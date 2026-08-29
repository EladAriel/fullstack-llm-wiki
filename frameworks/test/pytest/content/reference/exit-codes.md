---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/reference/exit-codes.rst"
source_commit: "fdba12e1708313f56e9cf713d260c029764ca2b7"
source_commit_short: "fdba12e"
source_commit_date: "2026-08-27T21:55:50+02:00"
generated_at: "2026-08-29T09:40:11.277485Z"
---
.. _exit-codes:

# Exit codes

Running ``pytest`` can result in seven different exit codes:

:Exit code 0: All tests were collected and passed successfully
:Exit code 1: Tests were collected and run but some of the tests failed
:Exit code 2: Test execution was interrupted by the user
:Exit code 3: Internal error happened while executing tests
:Exit code 4: pytest command line usage error
:Exit code 5: No tests were collected
:Exit code 6: Maximum number of warnings exceeded (see :option:`--max-warnings`)

They are represented by the :class:`pytest.ExitCode` enum. The exit codes being a part of the public API can be imported and accessed directly using:

.. code-block:: python

    from pytest import ExitCode

**note:** If you would like to customize the exit code in some scenarios, specifically when
    no tests are collected, consider using the
    `pytest-custom_exit_code <https://github.com/yashtodi94/pytest-custom_exit_code>`__
    plugin.