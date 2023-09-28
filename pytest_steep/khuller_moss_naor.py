# coding: utf-8

def _algorithm(test_id_to_duration, test_id_to_hit_indices, budget):
    i_to_Ti = [T for _, T in sorted(test_id_to_hit_indices.items())]
    i_to_ci = [t for _, t in sorted(test_id_to_duration.items())]
    index_to_test_id = {index: test_id for index, test_id in enumerate(sorted(test_id_to_duration))}
    L = budget

    # begin
    G = set()
    G_indices = set()
    G_indices_ordered = []
    U_indices = set(range(len(test_id_to_duration)))
    C = 0
    COV = 0
    while U_indices:
        best_i = None
        best_ci = None
        best_Wipci = -1
        best_cov_gain = None
        for i in U_indices:
            Wip = len(i_to_Ti[i].difference(G))
            ci = i_to_ci[i]
            Wipci = Wip / ci
            if Wipci > best_Wipci:
                best_i = i
                best_Wipci = Wipci
                best_ci = ci
                best_cov_gain = Wip
        if C + best_ci <= L:
            C += best_ci
            G_indices.add(best_i)
            G_indices_ordered.append(best_i)
            G.update(i_to_Ti[best_i])
            COV += best_cov_gain
        U_indices.remove(best_i)

    test_ids = {index_to_test_id[index] for index in G_indices}
    test_ids_ordered = [index_to_test_id[index] for index in G_indices_ordered]
    return test_ids_ordered, test_ids, C, COV

def algorithm(*a, **kw):
    _, test_ids, C, COV = _algorithm(*a, **kw)
    return test_ids, C, COV

def algorithm_ordered(*a, **kw):
    test_ids_ordered, _, C, COV = _algorithm(*a, **kw)
    return test_ids_ordered, C, COV
