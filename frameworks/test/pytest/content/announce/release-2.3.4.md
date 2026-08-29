---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.3.4.rst"
source_commit: "fdba12e1708313f56e9cf713d260c029764ca2b7"
source_commit_short: "fdba12e"
source_commit_date: "2026-08-27T21:55:50+02:00"
generated_at: "2026-08-29T09:40:11.182602Z"
---
# pytest-2.3.4: stabilization, more flexible selection via "-k expr"

pytest-2.3.4 is a small stabilization release of the py.test tool
which offers uebersimple assertions, scalable fixture mechanisms
and deep customization for testing with Python.  This release
comes with the following fixes and features:

- make "-k" option accept an expressions the same as with "-m" so that one
  can write: -k "name1 or name2" etc.  This is a slight usage incompatibility
  if you used special syntax like "TestClass.test_method" which you now
  need to write as -k "TestClass and test_method" to match a certain
  method in a certain test class.
- allow to dynamically define markers via
  item.keywords[...]=assignment integrating with "-m" option
- yielded test functions will now have autouse-fixtures active but
  cannot accept fixtures as funcargs - it's anyway recommended to
  rather use the post-2.0 parametrize features instead of yield, see:
  http://pytest.org/en/stable/example/how-to/parametrize.html
- fix autouse-issue where autouse-fixtures would not be discovered
  if defined in an a/conftest.py file and tests in a/tests/test_some.py
- fix issue226 - LIFO ordering for fixture teardowns
- fix issue224 - invocations with >256 char arguments now work
- fix issue91 - add/discuss package/directory level setups in example
- fixes related to autouse discovery and calling

Thanks in particular to Thomas Waldmann for spotting and reporting issues.

See

     http://pytest.org/

for general information.  To install or upgrade pytest:

    pip install -U pytest # or
    easy_install -U pytest

best,
holger krekel