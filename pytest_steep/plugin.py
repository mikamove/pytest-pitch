# -*- coding: utf-8 -*-

from pytest_donde.outcome import Outcome

from . import khuller_moss_naor as KMN

def pytest_addoption(parser):
    group = parser.getgroup('steep')
    group.addoption(
        '--steep',
        action='store_true',
        dest='steep_active',
        default=None,
        help='reorder tests for fast increase of coverage using donde json statics file.',
    )
    group.addoption(
        '--steep-in',
        action='store',
        dest='steep_donde_json_path',
        metavar='PATH',
        default='donde.json',
        help='PATH to donde json statics file, default is "donde.json".',
    )

def pytest_configure(config):
    if config.getoption('steep_active'):
        path = config.getoption('steep_donde_json_path')
        config.pluginmanager.register(SteepSelectorPlugin(path))

class SteepSelectorPlugin:

    def __init__(self, path_input):
        self._nodeids_changed = False
        self._nodeid_order = self._compute_optimal_order(path_input)

    def _compute_optimal_order(self, path_input):
        outcome = Outcome.from_file(path_input)

        budget = sum(outcome.nodeid_to_duration(nodeid) for nodeid in outcome.iter_nodeids())
        budget += 0.1 # circumvent float precision issues to ensure we catch all tests
        nindices, _, _ = KMN.algorithm_ordered(outcome.nindex_to_duration, outcome.nindex_to_lindices, budget)
        return [outcome.nodeids.from_index(nindex) for nindex in nindices]

    def pytest_collection_modifyitems(self, items, config):

        def key(item):
            try:
                return self._nodeid_order.index(item.nodeid)
            except ValueError:
                if not self._nodeids_changed:
                    self._nodeids_changed = True
                    # FIXME learn about pytest warning mechanism
                    path = config.getoption('steep_donde_json_path')
                    print(f'[steep] the test item {item.nodeid} was not registered in {path} and will be placed at the beginning, consider refreshing your donde json file to match your current test session.')
                return -1

        items[:] = sorted(items, key=key)
