# pytest_pitch

`pytest_pitch` runs tests in an order such that coverage increases as fast as possible. Typically 99% of the total coverage is achieved in 10% of the test session time.

![example](https://github.com/mikamove/pytest-steep/blob/main/example.png)

## en detail

- the coverage statistics is recorded with `pytest_donde` 

  This creates a `donde.json` file with the following information for every test item:
  - run duration (sec),
  - covered lines of code.

- then run your session with

    ```shell
    python -m pytest  <ANY ARGS> --pitch
	```

## use as a plugin

First create persistent time-coverage record via
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

## install

```shell
python -m pip install pytest_pitch
```
