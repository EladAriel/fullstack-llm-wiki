---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/reference/exit-codes.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# Exit codes

Running `pytest` can result in seven different exit codes:

:Exit code 0: All tests were collected and passed successfully :Exit code 1: Tests were collected and run but some of the tests failed :Exit code 2: Test execution was interrupted by the user :Exit code 3: Internal error happened while executing tests :Exit code 4: pytest command line usage error :Exit code 5: No tests were collected :Exit code 6: Maximum number of warnings exceeded (see :option:`--max-warnings`)

They are represented by the `pytest.ExitCode` enum. The exit codes being a part of the public API can be imported and accessed directly using:

```python
 from pytest import ExitCode
```

> **Note:**  If you would like to customize the exit code in some scenarios, specifically when
 no tests are collected, consider using the
 [pytest-custom_exit_code](https://github.com/yashtodi94/pytest-custom_exit_code)_
 plugin.
