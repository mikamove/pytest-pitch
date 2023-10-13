# pytest-pitch

`pytest-pitch` runs tests in an order such that coverage increases as fast as possible. Typically 99% of the total coverage is achieved in 10% of the test session time.

![example](https://github.com/mikamove/pytest-pitch/blob/main/example.png)

## Use case

The main use case is if **waiting for tests slows down Your development workflow**. In this case, if You let pitch reorder Your tests,
the whole session still takes the same time, but after 10% of this time You aready reach 99% line coverage
and thus can abort the session session - or go to Your next editing step - while the remaining 90% run,
**trading 1% residual risk for 90% time saving**.
Note that these numbers are based on experience, see below on how to visualize them for Your concrete project.

Tests with bad time scaling are a sign for bad code and/or test quality.
Tragically, for the necessary refactoring, one is even more tied to rely on these slow tests or even add more of them to increase coverage,
while the design doesn't allow for effective low-level unit tests.
This plugin serves as a helper for this painful transition. 

Its goal is to make itself unneccesary.

## Details

### use as pytest plugin for faster coverage increase

First create persistent time-coverage record via [pytest-donde](https://github.com/mikamove/pytest-donde)
```shell
python -m pytest [YOUR SESSION ARGS] --donde=/path/to/src
```
where `/path/to/src` is the code region to cover.

Then pass the record file to the plugin via
```shell
python -m pytest [YOUR SESSION ARGS] --pitch
```

If You change your test definitions or test selection `[YOUR SESSION ARGS]`
in step 2 without updating the record:
- tests which are unknown to step 1 (e.g. newly defined tests, less strict test selection)
  will be put to the start of the execution order
- tests which are known to step 1 but missing in step 2 (e.g. removed tests, stricter test selection) will just be filtered out. Any selection mechanisms should not conflict with the reordering.

### use algorithm API in your script

See [this script](https://github.com/mikamove/pytest-pitch/blob/main/scripts/benchmark_vs_project.py) as a demo which was used to create the image shown above.

## background

The plugin employs **Algorithm 1** from **p. 3** of
[S. Khuller, A. Moss, J. Naor, The budgeted maximum coverage problem, Inf. Process. Lett. 70, 1999](https://doi.org/10.1016/S0020-0190(99)00031-9).

## install

```shell
python -m pip install pytest-pitch
```
