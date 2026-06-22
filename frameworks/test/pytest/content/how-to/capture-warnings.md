---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/how-to/capture-warnings.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# How to capture warnings

Starting from version `3.1`, pytest now automatically catches warnings during test execution and displays them at the end of the session:

```python
 # content of test_show_warnings.py
 import warnings

 def api_v1():
     warnings.warn(UserWarning("api v1, should use functions from v2"))
     return 1

 def test_one():
     assert api_v1() == 1
```

Running pytest now produces this output:

```pytest
 $ pytest test_show_warnings.py
 =========================== test session starts ============================
 platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
 rootdir: /home/sweet/project
 collected 1 item

 test_show_warnings.py .                                              [100%]

 ============================= warnings summary =============================
 test_show_warnings.py::test_one
   /home/sweet/project/test_show_warnings.py:5: UserWarning: api v1, should use functions from v2
     warnings.warn(UserWarning("api v1, should use functions from v2"))

 -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
 ======================= 1 passed, 1 warning in 0.12s =======================
```

## Controlling warnings

Similar to Python's warning filter and :option:`-W option <python:-W>` flag, pytest provides its own `-W` flag to control which warnings are ignored, displayed, or turned into errors. See the warning filter documentation for more advanced use-cases.

This code sample shows how to treat any `UserWarning` category class of warning as an error:

```pytest
 $ pytest -q test_show_warnings.py -W error::UserWarning
 F                                                                    [100%]
 ================================= FAILURES =================================
 _________________________________ test_one _________________________________

     def test_one():
 >       assert api_v1() == 1
                ^^^^^^^^

 test_show_warnings.py:10:
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

     def api_v1():
 >       warnings.warn(UserWarning("api v1, should use functions from v2"))
 E       UserWarning: api v1, should use functions from v2

 test_show_warnings.py:5: UserWarning
 ========================= short test summary info ==========================
 FAILED test_show_warnings.py::test_one - UserWarning: api v1, should use ...
 1 failed in 0.12s
```

The same option can be set in the configuration file using the :confval:`filterwarnings` configuration option. For example, the configuration below will ignore all user warnings and specific deprecation warnings matching a regex, but will transform all other warnings into errors.

When a warning matches more than one option in the list, the action for the last matching option is performed.

> **Note:**  The `-W` flag and the :confval:`filterwarnings` configuration option use warning filters that are
 similar in structure, but each configuration option interprets its filter
 differently. For example, message in `filterwarnings` is a string containing a
 regular expression that the start of the warning message must match,
 case-insensitively, while message in `-W` is a literal string that the start of
 the warning message must contain (case-insensitively), ignoring any whitespace at
 the start or end of message. Consult the warning filter documentation for more
 details.

## `@pytest.mark.filterwarnings`

You can use the `@pytest.mark.filterwarnings <pytest.mark.filterwarnings ref>` mark to add warning filters to specific test items, allowing you to have finer control of which warnings should be captured at test, class or even module level:

```python
 import warnings

 def api_v1():
     warnings.warn(UserWarning("api v1, should use functions from v2"))
     return 1

 @pytest.mark.filterwarnings("ignore:api v1")
 def test_one():
     assert api_v1() == 1
```

You can specify multiple filters with separate decorators:

```python
 # Ignore "api v1" warnings, but fail on all other warnings
 @pytest.mark.filterwarnings("ignore:api v1")
 @pytest.mark.filterwarnings("error")
 def test_one():
     assert api_v1() == 1
```

You can also pass multiple filters to a single mark by providing multiple arguments:

```python
 # Later arguments take precedence, matching warnings.filterwarnings behavior.
 @pytest.mark.filterwarnings("error", "ignore:api v1")
 def test_one():
     assert api_v1() == 1
```

> **Important:**  Regarding decorator order and filter precedence:
 it's important to remember that decorators are evaluated in reverse order,
 so you have to list the warning filters in the reverse order
 compared to traditional `warnings.filterwarnings` and :option:`-W option <python:-W>` usage.
 This means in practice that filters from earlier `@pytest.mark.filterwarnings <pytest.mark.filterwarnings ref>` decorators
 take precedence over filters from later decorators, as illustrated in the example above.

Filters applied using a mark take precedence over filters passed on the command line or configured by the :confval:`filterwarnings` configuration option.

You may apply a filter to all tests of a class by using the `filterwarnings <pytest.mark.filterwarnings ref>` mark as a class decorator or to all tests in a module by setting the :globalvar:`pytestmark` variable:

```python
 # turns all warnings into errors for this module
 pytestmark = pytest.mark.filterwarnings("error")
```

> **Note:**  If you want to apply multiple filters
 (by assigning a list of `filterwarnings <pytest.mark.filterwarnings ref>` mark to :globalvar:`pytestmark`),
 you must use the traditional `warnings.filterwarnings` ordering approach (later filters take precedence),
 which is the reverse of the decorator approach mentioned above.

Credits go to Florian Schulze for the reference implementation in the pytest-warnings plugin.

## Setting a maximum number of warnings

.. versionadded:: 9.1

You can use the :option:`--max-warnings` command-line option to fail the test run if the total number of warnings exceeds a given threshold:

```bash
 pytest --max-warnings=10
```

If all tests pass but the number of warnings exceeds the threshold, pytest will exit with code `6` (`pytest.ExitCode` `MAX_WARNINGS_ERROR`). This is useful for gradually ratcheting down warnings in a codebase.

Note that :confval:`filtered warnings <filterwarnings>` do not count toward this maximum total.

The threshold can also be set in the configuration file using :confval:`max_warnings`:

> **Note:**  If tests fail, the exit code will be `1` (`pytest.ExitCode` `TESTS_FAILED`)
 regardless of the warning count. `MAX_WARNINGS_ERROR` is only reported when all tests pass
 but the warning threshold is exceeded.

## Disabling warnings summary

Although not recommended, you can use the :option:`--disable-warnings` command-line option to suppress the warning summary entirely from the test run output.

## Disabling warning capture entirely

This plugin is enabled by default but can be disabled entirely in your configuration file with:

Or passing `-p no:warnings` in the command-line. This might be useful if your test suite handles warnings using an external system.

## DeprecationWarning and PendingDeprecationWarning

By default pytest will display `DeprecationWarning` and `PendingDeprecationWarning` warnings from user code and third-party libraries, as recommended by `565`. This helps users keep their code modern and avoid breakages when deprecated warnings are effectively removed.

However, in the specific case where users capture any type of warnings in their test, either with `pytest.warns`, `pytest.deprecated_call` or using the :fixture:`recwarn` fixture, no warning will be displayed at all.

Sometimes it is useful to hide some specific deprecation warnings that happen in code that you have no control over (such as third-party libraries), in which case you might use the warning filters options (configuration or marks) to ignore those warnings.

For example:

This will ignore all warnings of type `DeprecationWarning` where the start of the message matches the regular expression `".U.mode is deprecated"`.

See `@pytest.mark.filterwarnings <filterwarnings>` and `Controlling warnings <controlling-warnings>` for more examples.

> **Note:**  If warnings are configured at the interpreter level, using
 the :envvar:`python:PYTHONWARNINGS` environment variable or the
 `-W` command-line option, pytest will not configure any filters by default.
 Also pytest doesn't follow `565` suggestion of resetting all warning filters because
 it might break test suites that configure warning filters themselves
 by calling `warnings.simplefilter` (see :issue:`2430` for an example of that).

## Ensuring code triggers a deprecation warning

You can also use `pytest.deprecated_call` for checking that a certain function call triggers a `DeprecationWarning`, `PendingDeprecationWarning` or `FutureWarning`:

```python
 import pytest

 def test_myfunction_deprecated():
     with pytest.deprecated_call():
         myfunction(17)
```

This test will fail if `myfunction` does not issue a deprecation warning when called with a `17` argument.

## Asserting warnings with the warns function

You can check that code raises a particular warning using `pytest.warns`, which works in a similar manner to `raises <assertraises>` (except that `raises <assertraises>` does not capture all exceptions, only the `expected_exception`):

```python
 import warnings

 import pytest

 def test_warning():
     with pytest.warns(UserWarning):
         warnings.warn("my warning", UserWarning)
```

The test will fail if the warning in question is not raised. Use the keyword argument `match` to assert that the warning matches a text or regex. To match a literal string that may contain regular expression metacharacters like `(` or `.`, the pattern can first be escaped with `re.escape`.

Some examples:

```pycon
 >>> with warns(UserWarning, match="must be 0 or None"):
 ...     warnings.warn("value must be 0 or None", UserWarning)
 ...

 >>> with warns(UserWarning, match=r"must be \d+$"):
 ...     warnings.warn("value must be 42", UserWarning)
 ...

 >>> with warns(UserWarning, match=r"must be \d+$"):
 ...     warnings.warn("this is not here", UserWarning)
 ...
 Traceback (most recent call last):
   ...
 Failed: Regex pattern did not match any of the 1 warnings emitted.
  Regex: ...
  Emitted warnings: ...UserWarning...

 >>> with warns(UserWarning, match=re.escape("issue with foo() func")):
 ...     warnings.warn("issue with foo() func")
 ...
```

The function also returns a list of all raised warnings (as `warnings.WarningMessage` objects), which you can query for additional information:

```python
 with pytest.warns(RuntimeWarning) as record:
     warnings.warn("another warning", RuntimeWarning)

 # check that only one warning was raised
 assert len(record) == 1
 # check that the message matches
 assert record[0].message.args[0] == "another warning"
```

Alternatively, you can examine raised warnings in detail using the :fixture:`recwarn` fixture (see `below <recwarn>`).

The :fixture:`recwarn` fixture automatically ensures to reset the warnings filter at the end of the test, so no global state is leaked.

## Recording warnings

You can record raised warnings either using the `pytest.warns` context manager or with the :fixture:`recwarn` fixture.

To record with `pytest.warns` without asserting anything about the warnings, pass no arguments as the expected warning type and it will default to a generic Warning:

```python
 with pytest.warns() as record:
     warnings.warn("user", UserWarning)
     warnings.warn("runtime", RuntimeWarning)

 assert len(record) == 2
 assert str(record[0].message) == "user"
 assert str(record[1].message) == "runtime"
```

The :fixture:`recwarn` fixture will record warnings for the whole function:

```python
 import warnings

 def test_hello(recwarn):
     warnings.warn("hello", UserWarning)
     assert len(recwarn) == 1
     w = recwarn.pop(UserWarning)
     assert issubclass(w.category, UserWarning)
     assert str(w.message) == "hello"
     assert w.filename
     assert w.lineno
```

Both the :fixture:`recwarn` fixture and the `pytest.warns context manager return the same interface for recorded warnings: a pytest.recwarn.WarningsRecorder` instance. To view the recorded warnings, you can iterate over this instance, call `len` on it to get the number of recorded warnings, or index into it to get a particular recorded warning.

## Additional use cases of warnings in tests

Here are some use cases involving warnings that often come up in tests, and suggestions on how to deal with them:

- To ensure that **at least one** of the indicated warnings is issued, use:
```python
 def test_warning():
     with pytest.warns((RuntimeWarning, UserWarning)):
         ...
```

- To ensure that **only** certain warnings are issued, use:
```python
 def test_warning(recwarn):
     ...
     assert len(recwarn) == 1
     user_warning = recwarn.pop(UserWarning)
     assert issubclass(user_warning.category, UserWarning)
```

- To ensure that **no** warnings are emitted, use:
```python
 def test_warning():
     with warnings.catch_warnings():
         warnings.simplefilter("error")
         ...
```

- To suppress warnings, use:
```python
 with warnings.catch_warnings():
     warnings.simplefilter("ignore")
     ...
```

## Custom failure messages

Recording warnings provides an opportunity to produce custom test failure messages for when no warnings are issued or other conditions are met.

```python
 def test():
     with pytest.warns(Warning) as record:
         f()
         if not record:
             pytest.fail("Expected a warning!")
```

If no warnings are issued when calling `f`, then `not record` will evaluate to `True`.  You can then call `pytest.fail` with a custom error message.

## Internal pytest warnings

pytest may generate its own warnings in some situations, such as improper usage or deprecated features.

For example, pytest will emit a warning if it encounters a class that matches :confval:`python_classes but also defines an _init__` constructor, as this prevents the class from being instantiated:

```python
 # content of test_pytest_warnings.py
 class Test:
     def __init__(self):
         pass

     def test_foo(self):
         assert 1 == 1
```

```pytest
 $ pytest test_pytest_warnings.py -q

 ============================= warnings summary =============================
 test_pytest_warnings.py:1
   /home/sweet/project/test_pytest_warnings.py:1: PytestCollectionWarning: cannot collect test class 'Test' because it has a __init__ constructor (from: test_pytest_warnings.py)
     class Test:

 -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
 1 warning in 0.12s
```

These warnings might be filtered using the same builtin mechanisms used to filter other types of warnings.

Please read our `backwards-compatibility` to learn how we proceed about deprecating and eventually removing features.

The full list of warnings is listed in `the reference documentation <warnings ref>`.

## Resource Warnings

Additional information of the source of a `ResourceWarning` can be obtained when captured by pytest if `tracemalloc` module is enabled.

One convenient way to enable `tracemalloc` when running tests is to set the :envvar:`PYTHONTRACEMALLOC` to a large enough number of frames (say `20`, but that number is application dependent).

For more information, consult the [Python Development Mode](https://docs.python.org/3/library/devmode.html)_ section in the Python documentation.
