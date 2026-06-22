---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/reference/reference.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

:tocdepth: 3

# API Reference

This page contains the full reference to pytest's API.

## Constants

### pytest.__version__

The current pytest version, as a string:

```
>>> import pytest
>>> pytest.__version__
'9.0.2'
```

### pytest.HIDDEN_PARAM

.. versionadded:: 8.4

Can be passed to `ids` of `Metafunc.parametrize <pytest.Metafunc.parametrize>` or to `id` of `pytest.param` to hide a parameter set from the test name. Can only be used at most 1 time, as test names need to be unique.

### pytest.version_tuple

.. versionadded:: 7.0

The current pytest version, as a tuple:

```
>>> import pytest
>>> pytest.version_tuple
(7, 0, 0)
```

For pre-releases, the last component will be a string with the prerelease version:

```
>>> import pytest
>>> pytest.version_tuple
(7, 0, '0rc1')
```

## Functions

### pytest.approx

### pytest.fail

**Tutorial**: `skipping`

### pytest.skip

### pytest.importorskip

### pytest.xfail

### pytest.exit

### pytest.main

**Tutorial**: `pytest.main-usage`

### pytest.param

### pytest.raises

**Tutorial**: `assertraises`

### pytest.deprecated_call

**Tutorial**: `ensuring_function_triggers`

### pytest.register_assert_rewrite

**Tutorial**: `assertion-rewriting`

### pytest.register_fixture

### pytest.warns

**Tutorial**: `assertwarnings`

### pytest.freeze_includes

**Tutorial**: `freezing-pytest`

## Marks

Marks can be used to apply metadata to test functions (but not fixtures), which can then be accessed by fixtures or plugins.

### pytest.mark.filterwarnings

**Tutorial**: `filterwarnings`

Add warning filters to marked test items.

:keyword str filter: A warning specification string, which is composed of contents of the tuple `(action, message, category, module, lineno)` as specified in `python:warning-filter` section of the Python documentation, separated by `":"`. Optional fields can be omitted. Module names passed for filtering are not regex-escaped.

For example:

```python
         @pytest.mark.filterwarnings(r"ignore:.*usage will be deprecated.*:DeprecationWarning")
         def test_foo(): ...
```

### pytest.mark.parametrize

**Tutorial**: `parametrize`

This mark has the same signature as `pytest.Metafunc.parametrize`; see there.

### pytest.mark.skip

**Tutorial**: `skip`

Unconditionally skip a test function.

:keyword str reason: Reason why the test function is being skipped.

### pytest.mark.skipif

**Tutorial**: `skipif`

Skip a test function if a condition is `True`.

:type condition: bool or str :param condition: `True/False` if the condition should be skipped or a `condition string <string conditions>`. :keyword str reason: Reason why the test function is being skipped.

### pytest.mark.usefixtures

**Tutorial**: `usefixtures`

Mark a test function as using the given fixture names.

:param args: The names of the fixture to use, as strings.

> **Note:**  When using `usefixtures` in hooks, it can only load fixtures when applied to a test function before test setup
 (for example in the `pytest_collection_modifyitems` hook).
 Also note that this mark has no effect when applied to **fixtures**.

### pytest.mark.xfail

**Tutorial**: `xfail`

Marks a test function as expected to fail.

:keyword Union[bool, str] condition: Condition for marking the test function as xfail (`True/False` or a `condition string <string conditions>`). If a `bool`, you also have to specify `reason` (see `condition string <string conditions>`). :keyword str reason: Reason why the test function is marked as xfail. :keyword raises: Exception class (or tuple of classes) expected to be raised by the test function; other exceptions will fail the test. Note that subclasses of the classes passed will also result in a match (similar to how the `except` statement works). :type raises: Type[:py`Exception`]

:keyword bool run: Whether the test function should actually be executed. If `False`, the function will always xfail and will not be executed (useful if a function is segfaulting). :keyword bool strict:

- If `False` the function will be shown in the terminal output as `xfailed` if it fails
and as `xpass` if it passes. In both cases this will not cause the test suite to fail as a whole. This is particularly useful to mark flaky tests (tests that fail at random) to be tackled later.

- If `True`, the function will be shown in the terminal output as `xfailed` if it fails, but if it
unexpectedly passes then it will **fail** the test suite. This is particularly useful to mark functions that are always failing and there should be a clear indication if they unexpectedly start to pass (for example a new release of a library fixes a known bug).

Defaults to :confval:`strict_xfail`, which is `False` by default.

### Custom marks

Marks are created dynamically using the factory object `pytest.mark` and applied as a decorator.

For example:

```python
 @pytest.mark.timeout(10, "slow", method="thread")
 def test_function(): ...
```

Will create and attach a `Mark <pytest.Mark>` object to the collected `Item <pytest.Item>`, which can then be accessed by fixtures or hooks with `Node.iter_markers <_pytest.nodes.Node.iter_markers>`. The `mark` object will have the following attributes:

```python
 mark.args == (10, "slow")
 mark.kwargs == {"method": "thread"}
```

Example for using multiple custom markers:

```python
 @pytest.mark.timeout(10, "slow", method="thread")
 @pytest.mark.slow
 def test_function(): ...
```

When `Node.iter_markers <_pytest.nodes.Node.iter_markers>` or `Node.iter_markers_with_node <_pytest.nodes.Node.iter_markers_with_node>` is used with multiple markers, the marker closest to the function will be iterated over first. The above example will result in `@pytest.mark.slow` followed by `@pytest.mark.timeout(...)`.

## Fixtures

**Tutorial**: `fixture`

Fixtures are requested by test functions or other fixtures by declaring them as argument names.

Example of a test requiring a fixture:

```python
 def test_output(capsys):
     print("hello")
     out, err = capsys.readouterr()
     assert out == "hello\n"
```

Example of a fixture requiring another fixture:

```python
 @pytest.fixture
 def db_session(tmp_path):
     fn = tmp_path / "db.file"
     return connect(fn)
```

For more details, consult the full `fixtures docs <fixture>`.

### @pytest.fixture

### capfd

**Tutorial**: `captures`

### capfdbinary

**Tutorial**: `captures`

### caplog

**Tutorial**: `logging`

### capsys

**Tutorial**: `captures`

### capteesys

**Tutorial**: `captures`

### capsysbinary

**Tutorial**: `captures`

### config.cache

**Tutorial**: `cache`

The `config.cache` object allows other plugins and fixtures to store and retrieve values across test runs. To access it from fixtures request `pytestconfig` into your fixture and get it with `pytestconfig.cache`.

Under the hood, the cache plugin uses the simple `dumps`/`loads` API of the `json` stdlib module.

`config.cache` is an instance of `pytest.Cache`:

### doctest_namespace

**Tutorial**: `doctest`

### monkeypatch

**Tutorial**: `monkeypatching`

### pytestconfig

### pytester

.. versionadded:: 6.2

Provides a `pytest.Pytester` instance that can be used to run and test pytest itself.

It provides an empty directory where pytest can be executed in isolation, and contains facilities to write tests, configuration files, and match against expected output.

To use it, include in your topmost `conftest.py` file:

```python
 pytest_plugins = "pytester"
```

### record_property

**Tutorial**: `record_property example`

### record_testsuite_property

**Tutorial**: `record_testsuite_property example`

### recwarn

**Tutorial**: `recwarn`

### request

**Example**: `request example`

The `request` fixture is a special fixture providing information of the requesting test function.

### subtests

The `subtests` fixture enables declaring subtests inside test functions.

**Tutorial**: `subtests`

### testdir

Identical to :fixture:`pytester`, but provides an instance whose methods return legacy `py.path.local` objects instead when applicable.

New code should avoid using :fixture:`testdir` in favor of :fixture:`pytester`.

### tmp_path

**Tutorial**: `tmp_path`

### tmp_path_factory

**Tutorial**: `tmp_path_factory example`

`tmp_path_factory` is an instance of `pytest.TempPathFactory`:

### tmpdir

**Tutorial**: `tmpdir and tmpdir_factory`

### tmpdir_factory

**Tutorial**: `tmpdir and tmpdir_factory`

`tmpdir_factory` is an instance of `pytest.TempdirFactory`:

## Hooks

**Tutorial**: `writing-plugins`

Reference to all hooks which can be implemented by `conftest.py files <localplugin>` and `plugins <plugins>`.

### @pytest.hookimpl

### @pytest.hookspec

### Bootstrapping hooks

Bootstrapping hooks called for plugins registered early enough (internal and third-party plugins).

### Initialization hooks

Initialization hooks called for plugins and `conftest.py` files.

### Collection hooks

`pytest` calls the following hooks for collecting files and directories:

For influencing the collection of objects in Python modules you can use the following hook:

Hooks for influencing test skipping:

After collection is complete, you can modify the order of items, delete or otherwise amend the test items:

> **Note:**  If this hook is implemented in `conftest.py` files, it always receives all collected items, not only those
 under the `conftest.py` where it is implemented.

### Test running (runtest) hooks

All runtest related hooks receive a `pytest.Item <pytest.Item>` object.

For deeper understanding you may look at the default implementation of these hooks in `_pytest.runner and maybe also in pytest.pdb which interacts with pytest.capture` and its input/output capturing in order to immediately drop into interactive debugging when a test failure occurs.

### Reporting hooks

Session related reporting hooks:

Central hook for reporting about test execution:

Assertion related hooks:

### Debugging/Interaction hooks

There are few hooks which can be used for special reporting or interaction with exceptions:

## Collection tree objects

These are the collector and item classes (collectively called "nodes") which make up the collection tree.

### Node

### Collector

### Item

### File

### FSCollector

### Session

### Package

### Module

### Class

### Function

### FunctionDefinition

## Objects

Objects accessible from `fixtures <fixture>` or `hooks <hook-reference>` or importable from `pytest`.

### CallInfo

### CollectReport

### Config

### Dir

### Directory

### ExceptionInfo

### ExitCode

### FixtureDef

### MarkDecorator

### MarkGenerator

### Mark

### Metafunc

### Parser

### OptionGroup

### PytestPluginManager

### RaisesExc

### RaisesGroup

**Tutorial**: `assert-matching-exception-groups`

### TerminalReporter

### TestReport

### TestShortLogReport

### Result

Result object used within `hook wrappers <hookwrapper>`, see `Result in the pluggy documentation <pluggy.Result>` for more information.

### Stash

## Global Variables

pytest treats some global variables in a special manner when defined in a test module or `conftest.py` files.

**Tutorial**: `customizing-test-collection`

Can be declared in conftest.py files to exclude test directories or modules. Needs to be a list of paths (`str`, `pathlib.Path` or any `os.PathLike`).

```python
collect_ignore = ["setup.py"]
```

**Tutorial**: `customizing-test-collection`

Can be declared in conftest.py files to exclude test directories or modules with Unix shell-style wildcards. Needs to be `list[str]` where `str` can contain glob patterns.

```python
collect_ignore_glob = ["*_ignore.py"]
```

**Tutorial**: `available installable plugins`

Can be declared at the **global** level in test modules and conftest.py files to register additional plugins. Can be either a `str` or `Sequence[str]`.

```python
 pytest_plugins = "myapp.testsupport.myplugin"
```

```python
 pytest_plugins = ("myapp.testsupport.tools", "myapp.testsupport.regression")
```

**Tutorial**: `scoped-marking`

Can be declared at the **global** level in test modules to apply one or more `marks <marks ref>` to all test functions and methods. Can be either a single mark or a list of marks (applied in left-to-right order).

```python
 import pytest

 pytestmark = pytest.mark.webtest
```

```python
 import pytest

 pytestmark = [pytest.mark.integration, pytest.mark.slow]
```

## Environment Variables

Environment variables that can be used to change pytest's behavior.

## Exceptions

## Warnings

Custom warnings generated in some situations such as improper usage or deprecated features.

Consult the `internal-warnings` section in the documentation for more information.

## Configuration Options

Here is a list of builtin configuration options that may be written in a `pytest.ini` (or `.pytest.ini`), `pyproject.toml`, `tox.ini`, or `setup.cfg` file, usually located at the root of your repository.

To see each file format in detail, see `config file formats`.

> **Warning:**  Usage of `setup.cfg` is not recommended except for very simple use cases. `.cfg`
 files use a different parser than `pytest.ini` and `tox.ini` which might cause hard to track
 down problems.
 When possible, it is recommended to use the latter files, or `pytest.toml` or `pyproject.toml`, to hold your pytest configuration.

Configuration options may be overwritten in the command-line by using `-o/--override-ini`, which can also be passed multiple times. The expected format is `name=value`. For example:

```
pytest -o console_output_style=classic -o cache_dir=/tmp/mycache
```

## Command-line Flags

This section documents all command-line options provided by pytest's core plugins.

> **Note:**  External plugins can add their own command-line options.
 This reference documents only the options from pytest's core plugins.
 To see all available options including those from installed plugins, run `pytest --help`.

### Test Selection

### Test Execution Control

### Collection

### Fixtures

### Debugging

### Output and Reporting

### Output Capture

### JUnit XML

### Cache

### Warnings

### Doctest

### Configuration

### Logging

See `logging` for a guide on using these flags.

### Plugin and Extension Management

### Version and Help

### Complete Help Output

All the command-line flags can also be obtained by running `pytest --help`:

```
$ pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

positional arguments:
  file_or_dir

general:
  -k EXPRESSION         Only run tests which match the given substring
                        expression. An expression is a Python evaluable
                        expression where all names are substring-matched
                        against test names and their parent classes.
                        Example: -k 'test_method or test_other' matches all
                        test functions and classes whose name contains
                        'test_method' or 'test_other', while -k 'not
                        test_method' matches those that don't contain
                        'test_method' in their names. -k 'not test_method
                        and not test_other' will eliminate the matches.
                        Additionally keywords are matched to classes and
                        functions containing extra names in their
                        'extra_keyword_matches' set, as well as functions
                        which have names assigned directly to them. The
                        matching is case-insensitive.
  -m MARKEXPR           Only run tests matching given mark expression. For
                        example: -m 'mark1 and not mark2'.
  --markers             show markers (builtin, plugin and per-project ones).
  -x, --exitfirst       Exit instantly on first error or failed test
  --maxfail=num         Exit after first num failures or errors
  --strict-config       Enables the strict_config option
  --strict-markers      Enables the strict_markers option
  --strict              Enables the strict option
  --fixtures, --funcargs
                        Show available fixtures, sorted by plugin appearance
                        (fixtures with leading '_' are only shown with '-v')
  --fixtures-per-test   Show fixtures per test
  --pdb                 Start the interactive Python debugger on errors or
                        KeyboardInterrupt
  --pdbcls=modulename:classname
                        Specify a custom interactive Python debugger for use
                        with --pdb.For example:
                        --pdbcls=IPython.terminal.debugger:TerminalPdb
  --trace               Immediately break when running each test
  --capture=method      Per-test capturing method: one of fd|sys|no|tee-sys
  -s                    Shortcut for --capture=no
  --runxfail            Report the results of xfail tests as if they were
                        not marked
  --lf, --last-failed   Rerun only the tests that failed at the last run (or
                        all if none failed)
  --ff, --failed-first  Run all tests, but run the last failures first. This
                        may re-order tests and thus lead to repeated fixture
                        setup/teardown.
  --nf, --new-first     Run tests from new files first, then the rest of the
                        tests sorted by file mtime
  --cache-show=[CACHESHOW]
                        Show cache contents, don't perform collection or
                        tests. Optional argument: glob (default: '*').
  --cache-clear         Remove all cache contents at start of test run
  --lfnf, --last-failed-no-failures={all,none}
                        With ``--lf``, determines whether to execute tests
                        when there are no previously (known) failures or
                        when no cached ``lastfailed`` data was found.
                        ``all`` (the default) runs the full test suite
                        again. ``none`` just emits a message about no known
                        failures and exits successfully.
  --sw, --stepwise      Exit on test failure and continue from last failing
                        test next time
  --sw-skip, --stepwise-skip
                        Ignore the first failing test but stop on the next
                        failing test. Implicitly enables --stepwise.
  --sw-reset, --stepwise-reset
                        Resets stepwise state, restarting the stepwise
                        workflow. Implicitly enables --stepwise.

Reporting:
  --durations=N         Show N slowest setup/test durations (N=0 for all)
  --durations-min=N     Minimal duration in seconds for inclusion in slowest
                        list. Default: 0.005 (or 0.0 if -vv is given).
  -v, --verbose         Increase verbosity
  --no-header           Disable header
  --no-summary          Disable summary
  --no-fold-skipped     Do not fold skipped tests in short summary.
  --force-short-summary
                        Force condensed summary output regardless of
                        verbosity level.
  -q, --quiet           Decrease verbosity
  --verbosity=VERBOSE   Set verbosity. Default: 0.
  -r, --report-chars chars
                        Show extra test summary info as specified by chars:
                        (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
                        (p)assed, (P)assed with output, (a)ll except passed
                        (p/P), or (A)ll. (w)arnings are enabled by default
                        (see --disable-warnings), 'N' can be used to reset
                        the list. (default: 'fE').
  --disable-warnings, --disable-pytest-warnings
                        Disable warnings summary
  -l, --showlocals      Show locals in tracebacks (disabled by default)
  --no-showlocals       Hide locals in tracebacks (negate --showlocals
                        passed through addopts)
  --tb=style            Traceback print mode
                        (auto/long/short/line/native/no)
  --xfail-tb            Show tracebacks for xfail (as long as --tb != no)
  --show-capture={no,stdout,stderr,log,all}
                        Controls how captured stdout/stderr/log is shown on
                        failed tests. Default: all.
  --full-trace          Don't cut any tracebacks (default is to cut)
  --color=color         Color terminal output (yes/no/auto)
  --code-highlight={yes,no}
                        Whether code should be highlighted (only if --color
                        is also enabled). Default: yes.
  --pastebin=mode       Send failed|all info to bpaste.net pastebin service
  --junitxml, --junit-xml=path
                        Create junit-xml style report file at given path
  --junitprefix, --junit-prefix=str
                        Prepend prefix to classnames in junit-xml output

pytest-warnings:
  -W, --pythonwarnings PYTHONWARNINGS
                        Set which warnings to report, see -W option of
                        Python itself
  --max-warnings=num    Exit with error if all tests pass but the number of
                        warnings exceeds this threshold

collection:
  --collect-only, --co  Only collect tests, don't execute them
  --pyargs              Try to interpret all arguments as Python packages
  --ignore=path         Ignore path during collection (multi-allowed)
  --ignore-glob=path    Ignore path pattern during collection (multi-
                        allowed)
  --deselect=nodeid_prefix
                        Deselect item (via node id prefix) during collection
                        (multi-allowed)
  --confcutdir=dir      Only load conftest.py's relative to specified dir
  --noconftest          Don't load any conftest.py files
  --keep-duplicates     Keep duplicate tests
  --collect-in-virtualenv
                        Don't ignore tests in a local virtualenv directory
  --continue-on-collection-errors
                        Force test execution even if collection errors occur
  --import-mode={prepend,append,importlib}
                        Prepend/append to sys.path when importing test
                        modules and conftest files. Default: prepend.
  --doctest-modules     Run doctests in all .py modules
  --doctest-report={none,cdiff,ndiff,udiff,only_first_failure}
                        Choose another output format for diffs on doctest
                        failure
  --doctest-glob=pat    Doctests file matching pattern, default: test*.txt
  --doctest-ignore-import-errors
                        Ignore doctest collection errors
  --doctest-continue-on-failure
                        For a given doctest, continue to run after the first
                        failure

test session debugging and configuration:
  -c, --config-file FILE
                        Load configuration from `FILE` instead of trying to
                        locate one of the implicit configuration files.
  --rootdir=ROOTDIR     Define root directory for tests. Can be relative
                        path: 'root_dir', './root_dir',
                        'root_dir/another_dir/'; absolute path:
                        '/home/user/root_dir'; path with variables:
                        '$HOME/root_dir'.
  --basetemp=dir        Base temporary directory for this test run.
                        (Warning: this directory is removed if it exists.)
  -V, --version         Display pytest version and information about
                        plugins. When given twice, also display information
                        about plugins.
  -h, --help            Show help message and configuration info
  -p name               Early-load given plugin module name or entry point
                        (multi-allowed). To avoid loading of plugins, use
                        the `no:` prefix, e.g. `no:doctest`. See also
                        --disable-plugin-autoload.
  --disable-plugin-autoload
                        Disable plugin auto-loading through entry point
                        packaging metadata. Only plugins explicitly
                        specified in -p or env var PYTEST_PLUGINS will be
                        loaded.
  --trace-config        Trace considerations of conftest.py files
  --debug=[DEBUG_FILE_NAME]
                        Store internal tracing debug information in this log
                        file. This file is opened with 'w' and truncated as
                        a result, care advised. Default: pytestdebug.log.
  -o, --override-ini OVERRIDE_INI
                        Override configuration option with "option=value"
                        style, e.g. `-o strict_xfail=True -o
                        cache_dir=cache`.
  --assert=MODE         Control assertion debugging tools.
                        'plain' performs no assertion debugging.
                        'rewrite' (the default) rewrites assert statements
                        in test modules on import to provide assert
                        expression information.
  --setup-only          Only setup fixtures, do not execute tests
  --setup-show          Show setup of fixtures while executing tests
  --setup-plan          Show what fixtures and tests would be executed but
                        don't execute anything

logging:
  --log-level=LEVEL     Level of messages to catch/display. Not set by
                        default, so it depends on the root/parent log
                        handler's effective level, where it is "WARNING" by
                        default.
  --log-format=LOG_FORMAT
                        Log format used by the logging module
  --log-date-format=LOG_DATE_FORMAT
                        Log date format used by the logging module
  --log-cli-level=LOG_CLI_LEVEL
                        CLI logging level
  --log-cli-format=LOG_CLI_FORMAT
                        Log format used by the logging module
  --log-cli-date-format=LOG_CLI_DATE_FORMAT
                        Log date format used by the logging module
  --log-file=LOG_FILE   Path to a file when logging will be written to
  --log-file-mode={w,a}
                        Log file open mode
  --log-file-level=LOG_FILE_LEVEL
                        Log file logging level
  --log-file-format=LOG_FILE_FORMAT
                        Log format used by the logging module
  --log-file-date-format=LOG_FILE_DATE_FORMAT
                        Log date format used by the logging module
  --log-auto-indent=LOG_AUTO_INDENT
                        Auto-indent multiline messages passed to the logging
                        module. Accepts true|on, false|off or an integer.
  --log-disable=LOGGER_DISABLE
                        Disable a logger by name. Can be passed multiple
                        times.

[pytest] configuration options in the first pytest.toml|pytest.ini|tox.ini|setup.cfg|pyproject.toml file found:

  markers (linelist):   Register new markers for test functions
  empty_parameter_set_mark (string):
                        Default marker for empty parametersets
  strict_config (bool): Any warnings encountered while parsing the `pytest`
                        section of the configuration file raise errors
  strict_markers (bool):
                        Markers not registered in the `markers` section of
                        the configuration file raise errors
  strict (bool):        Enables all strictness options, currently:
                        strict_config, strict_markers, strict_xfail,
                        strict_parametrization_ids
  filterwarnings (linelist):
                        Each line specifies a pattern for
                        warnings.filterwarnings. Processed after
                        -W/--pythonwarnings.
  max_warnings (string):
                        Exit with error if all tests pass but the number of
                        warnings exceeds this threshold
  norecursedirs (args): Directory patterns to avoid for recursion
  testpaths (args):     Directories to search for tests when no files or
                        directories are given on the command line
  collect_imported_tests (bool):
                        Whether to collect tests in imported modules outside
                        `testpaths`
  consider_namespace_packages (bool):
                        Consider namespace packages when resolving module
                        names during import
  usefixtures (args):   List of default fixtures to be used with this
                        project
  python_files (args):  Glob-style file patterns for Python test module
                        discovery
  python_classes (args):
                        Prefixes or glob names for Python test class
                        discovery
  python_functions (args):
                        Prefixes or glob names for Python test function and
                        method discovery
  disable_test_id_escaping_and_forfeit_all_rights_to_community_support (bool):
                        Disable string escape non-ASCII characters, might
                        cause unwanted side effects(use at your own risk)
  strict_parametrization_ids (bool):
                        Emit an error if non-unique parameter set IDs are
                        detected
  console_output_style (string):
                        Console output: "classic", or with additional
                        progress information ("progress" (percentage) |
                        "count" | "progress-even-when-capture-no" (forces
                        progress even when capture=no)
  verbosity_test_cases (string):
                        Specify a verbosity level for test case execution,
                        overriding the main level. Higher levels will
                        provide more detailed information about each test
                        case executed.
  strict_xfail (bool):  Default for the strict parameter of xfail markers
                        when not given explicitly (default: False) (alias:
                        xfail_strict)
  tmp_path_retention_count (string):
                        How many sessions should we keep the `tmp_path`
                        directories, according to
                        `tmp_path_retention_policy`.
  tmp_path_retention_policy (string):
                        Controls which directories created by the `tmp_path`
                        fixture are kept around, based on test outcome.
                        (all/failed/none)
  enable_assertion_pass_hook (bool):
                        Enables the pytest_assertion_pass hook. Make sure to
                        delete any previously generated pyc cache files.
  truncation_limit_lines (string):
                        Set threshold of LINES after which truncation will
                        take effect
  truncation_limit_chars (string):
                        Set threshold of CHARS after which truncation will
                        take effect
  assertion_text_diff_style (string):
                        Choose how pytest renders diffs for string equality
                        assertions: ndiff or block
  verbosity_assertions (string):
                        Specify a verbosity level for assertions, overriding
                        the main level. Higher levels will provide more
                        detailed explanation when an assertion fails.
  junit_suite_name (string):
                        Test suite name for JUnit report
  junit_logging (string):
                        Write captured log messages to JUnit report: one of
                        no|log|system-out|system-err|out-err|all
  junit_log_passing_tests (bool):
                        Capture log information for passing tests to JUnit
                        report:
  junit_duration_report (string):
                        Duration time to report: one of total|call
  junit_family (string):
                        Emit XML for schema: one of legacy|xunit1|xunit2
  doctest_optionflags (args):
                        Option flags for doctests
  doctest_encoding (string):
                        Encoding used for doctest files
  cache_dir (string):   Cache directory path
  log_level (string):   Default value for --log-level
  log_format (string):  Default value for --log-format
  log_date_format (string):
                        Default value for --log-date-format
  log_cli (bool):       Enable log display during test run (also known as
                        "live logging")
  log_cli_level (string):
                        Default value for --log-cli-level
  log_cli_format (string):
                        Default value for --log-cli-format
  log_cli_date_format (string):
                        Default value for --log-cli-date-format
  log_file (string):    Default value for --log-file
  log_file_mode (string):
                        Default value for --log-file-mode
  log_file_level (string):
                        Default value for --log-file-level
  log_file_format (string):
                        Default value for --log-file-format
  log_file_date_format (string):
                        Default value for --log-file-date-format
  log_auto_indent (string):
                        Default value for --log-auto-indent
  faulthandler_timeout (string):
                        Dump the traceback of all threads if a test takes
                        more than TIMEOUT seconds to finish
  faulthandler_exit_on_timeout (bool):
                        Exit the test process if a test takes more than
                        faulthandler_timeout seconds to finish
  verbosity_subtests (string):
                        Specify verbosity level for subtests. Higher levels
                        will generate output for passed subtests. Failed
                        subtests are always reported.
  addopts (args):       Extra command line options
  minversion (string):  Minimally required pytest version
  pythonpath (paths):   Add paths to sys.path
  required_plugins (args):
                        Plugins that must be present for pytest to run

Environment variables:
  CI                       When set to a non-empty value, pytest knows it is running in a CI process and does not truncate summary info
  BUILD_NUMBER             Equivalent to CI
  PYTEST_ADDOPTS           Extra command line options
  PYTEST_PLUGINS           Comma-separated plugins to load during startup
  PYTEST_DISABLE_PLUGIN_AUTOLOAD Set to disable plugin auto-loading
  PYTEST_DEBUG             Set to enable debug tracing of pytest's internals
  PYTEST_DEBUG_TEMPROOT    Override the system temporary directory
  PYTEST_THEME             The Pygments style to use for code output
  PYTEST_THEME_MODE        Set the PYTEST_THEME to be either 'dark' or 'light'

to see available markers type: pytest --markers
to see available fixtures type: pytest --fixtures
(shown according to specified file_or_dir or current dir if not specified; fixtures with leading '_' are only shown with the '-v' option
```
