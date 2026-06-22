---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.6.3.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# pytest-2.6.3: fixes and little improvements

pytest is a mature Python testing tool with more than 1100 tests against itself, passing on many different interpreters and platforms. This release is drop-in compatible to 2.5.2 and 2.6.X. See below for the changes and see docs at:

http://pytest.org

As usual, you can upgrade from pypi via:

```
pip install -U pytest
```

Thanks to all who contributed, among them:

Floris Bruynooghe Oleg Sinyavskiy Uwe Schmitt Charles Cloud Wolfgang Schnerring

have fun, holger krekel

# Changes 2.6.3

- fix issue575: xunit-xml was reporting collection errors as failures
instead of errors, thanks Oleg Sinyavskiy.

- fix issue582: fix setuptools example, thanks Laszlo Papp and Ronny
Pfannschmidt.

- Fix infinite recursion bug when pickling capture.EncodedFile, thanks
Uwe Schmitt.

- fix issue589: fix bad interaction with numpy and others when showing
exceptions.  Check for precise "maximum recursion depth exceed" exception instead of presuming any RuntimeError is that one (implemented in py dep).  Thanks Charles Cloud for analysing the issue.

- fix conftest related fixture visibility issue: when running with a
CWD outside of a test package pytest would get fixture discovery wrong. Thanks to Wolfgang Schnerring for figuring out a reproducible example.

- Introduce pytest_enter_pdb hook (needed e.g. by pytest_timeout to cancel the
timeout when interactively entering pdb).  Thanks Wolfgang Schnerring.

- check xfail/skip also with non-python function test items. Thanks
Floris Bruynooghe.
