---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.6.1.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# pytest-2.6.1: fixes and new xfail feature

pytest is a mature Python testing tool with more than 1100 tests against itself, passing on many different interpreters and platforms. The 2.6.1 release is drop-in compatible to 2.5.2 and actually fixes some regressions introduced with 2.6.0.  It also brings a little feature to the xfail marker which now recognizes expected exceptions, see the CHANGELOG below.

See docs at:

http://pytest.org

As usual, you can upgrade from pypi via:

```
pip install -U pytest
```

Thanks to all who contributed, among them:

Floris Bruynooghe Bruno Oliveira Nicolas Delaby

have fun, holger krekel

# Changes 2.6.1

- No longer show line numbers in the --verbose output, the output is now
purely the nodeid.  The line number is still shown in failure reports. Thanks Floris Bruynooghe.

- fix issue437 where assertion rewriting could cause pytest-xdist worker nodes
to collect different tests. Thanks Bruno Oliveira.

- fix issue555: add "errors" attribute to capture-streams to satisfy
some distutils and possibly other code accessing sys.stdout.errors.

- fix issue547 capsys/capfd also work when output capturing ("-s") is disabled.
- address issue170: allow pytest.mark.xfail(...) to specify expected exceptions via
an optional "raises=EXC" argument where EXC can be a single exception or a tuple of exception classes.  Thanks David Mohr for the complete PR.

- fix integration of pytest with unittest.mock.patch decorator when
it uses the "new" argument.  Thanks Nicolas Delaby for test and PR.

- fix issue with detecting conftest files if the arguments contain
"::" node id specifications (copy pasted from "-v" output)

- fix issue544 by only removing "@NUM" at the end of "::" separated parts
and if the part has a ".py" extension

- don't use py.std import helper, rather import things directly.
Thanks Bruno Oliveira.
