---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/how-to/usage.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# How to invoke pytest

> **Seealso:**

In general, pytest is invoked with the command `pytest` (see below for `other ways to invoke pytest <invoke-other>`). This will execute all tests in all files whose names follow the form `test_.py` or `_test.py` in the current directory and its subdirectories. More generally, pytest follows `standard test discovery rules <test discovery>`.

## Specifying which tests to run

Pytest supports several ways to run and select tests from the command-line or from a file (see below for `reading arguments from file <args-from-file>`).

**Run tests in a module**

```bash
 pytest test_mod.py
```

**Run tests in a directory**

```bash
 pytest testing/
```

**Run tests by keyword expressions**

```bash
 pytest -k 'MyClass and not method'
```

This will run tests which contain names that match the given string expression (case-insensitive), which can include Python operators that use filenames, class names and function names as variables. The example above will run `TestMyClass.test_something`  but not `TestMyClass.test_method_simple`. Use `""` instead of `''` in expression when running this on Windows

**Run tests by collection arguments**

Pass the module filename relative to the working directory, followed by specifiers like the class name and function name separated by `::` characters, and parameters from parameterization enclosed in `[]`.

To run a specific test within a module:

```bash
 pytest tests/test_mod.py::test_func
```

To run all tests in a class:

```bash
 pytest tests/test_mod.py::TestClass
```

Specifying a specific test method:

```bash
 pytest tests/test_mod.py::TestClass::test_method
```

Specifying a specific parametrization of a test:

```bash
 pytest tests/test_mod.py::test_func[x1,y2]
```

**Run tests by marker expressions**

To run all tests which are decorated with the `@pytest.mark.slow` decorator:

```bash
 pytest -m slow
```

To run all tests which are decorated with the annotated `@pytest.mark.slow(phase=1)` decorator, with the `phase` keyword argument set to `1`:

```bash
 pytest -m "slow(phase=1)"
```

For more information see `marks <mark>`.

**Run tests from packages**

```bash
 pytest --pyargs pkg.testing
```

This will import `pkg.testing` and use its filesystem location to find and run tests from.

**Read arguments from file**

.. versionadded:: 8.2

All of the above can be read from a file using the `@` prefix:

```bash
 pytest @tests_to_run.txt
```

where `tests_to_run.txt` contains an entry per line, e.g.:

```text
 tests/test_file.py
 tests/test_mod.py::test_func[x1,y2]
 tests/test_mod.py::TestClass
 -m slow
```

This file can also be generated using `pytest --collect-only -q` and modified as needed.

## Getting help on version, option names, environment variables

```bash
 pytest --version   # shows where pytest was imported from
 pytest --fixtures  # show available builtin function arguments
 pytest -h | --help # show help on command line and config file options
```

## Profiling test execution duration

.. versionchanged:: 6.0

To get a list of the slowest 10 test durations over 1.0s long:

```bash
 pytest --durations=10 --durations-min=1.0
```

By default, pytest will not show test durations that are too small (<0.005s) unless `-vv` is passed on the command-line.

## Managing loading of plugins

### Early loading plugins

You can early-load plugins (internal and external) explicitly in the command-line with the :option:`-p` option:

```
pytest -p mypluginmodule
```

The option receives a `name` parameter, which can be:

- A full module dotted name, for example `myproject.plugins`. This dotted name must be importable.
- The entry-point name of a plugin. This is the name passed to `importlib` when the plugin is
registered. For example to early-load the :pypi:`pytest-cov` plugin you can use:

```
pytest -p pytest_cov
```

### Disabling plugins

To disable loading specific plugins at invocation time, use the :option:`-p` option together with the prefix `no:`.

Example: to disable loading the plugin `doctest`, which is responsible for executing doctest tests from text files, invoke pytest like this:

```bash
 pytest -p no:doctest
```

## Other ways of calling pytest

### Calling pytest through `python -m pytest`

You can invoke testing through the Python interpreter from the command line:

```text
 python -m pytest [...]
```

This is almost equivalent to invoking the command line script `pytest [...]` directly, except that calling via `python` will also add the current directory to `sys.path`.

### Calling pytest from Python code

You can invoke `pytest` from Python code directly:

```python
 retcode = pytest.main()
```

this acts as if you would call "pytest" from the command line. It will not raise `SystemExit` but return the `exit code <exit-codes>` instead. If you don't pass it any arguments, `main` reads the arguments from the command line arguments of the process (`sys.argv`), which may be undesirable. You can pass in options and arguments explicitly:

```python
 retcode = pytest.main(["-x", "mytestdir"])
```

You can specify additional plugins to `pytest.main`:

```python
 # content of myinvoke.py
 import sys

 import pytest

 class MyPlugin:
     def pytest_sessionfinish(self):
         print("*** test run reporting finishing")

 if __name__ == "__main__":
     sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))
```

Running it will show that `MyPlugin` was added and its hook was invoked:

```pytest
 $ python myinvoke.py
 *** test run reporting finishing
```

> **Note:**  Calling `pytest.main()` will result in importing your tests and any modules
 that they import. Due to the caching mechanism of python's import system,
 making subsequent calls to `pytest.main()` from the same process will not
 reflect changes to those files between the calls. For this reason, making
 multiple calls to `pytest.main()` from the same process (in order to re-run
 tests, for example) is not recommended.
