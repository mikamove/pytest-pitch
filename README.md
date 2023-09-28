# pytest_steep

`pytest_steep` runs tests in an order such that coverage increases as fast as possible. Typically 99% of the total coverage is achieved in 10% of the test session time.

![example](https://github.com/mikamove/pytest-steep/blob/main/example.png)

## en detail

- the coverage statistics is recorded with `pytest_donde` 

    ```shell
    python -m pytest --donde=/path/to/src
	```
  This creates a `donde.json` file with the following information for every test item:
  - run duration (sec),
  - covered lines of code.

- then run your session with

    ```shell
    python -m pytest  <ANY ARGS> --steep
	```

## install

```shell
python -m pip install pytest_steep
```
