---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.3.1.rst"
source_commit: "344c23787cdb3431dcc441b8b63ee9950f04b921"
source_commit_short: "344c2378"
source_commit_date: "2026-07-24T17:37:16+02:00"
generated_at: "2026-07-25T11:50:13Z"
---

# pytest-2.3.1: fix regression with factory functions

pytest-2.3.1 is a quick follow-up release:

- fix issue202 - regression with fixture functions/funcarg factories:
using "self" is now safe again and works as in 2.2.4.  Thanks to Eduard Schettino for the quick bug report.

- disable pexpect pytest self tests on Freebsd - thanks Koob for the
quick reporting

- fix/improve interactive docs with --markers
See

http://pytest.org/

for general information.  To install or upgrade pytest:

pip install -U pytest # or easy_install -U pytest

best, holger krekel

## Changes between 2.3.0 and 2.3.1

- fix issue202 - fix regression: using "self" from fixture functions now
works as expected (it's the same "self" instance that a test method which uses the fixture sees)

- skip pexpect using tests (test_pdb.py mostly) on freebsd* systems
due to pexpect not supporting it properly (hanging)

- link to web pages from --markers output which provides help for
pytest.mark.* usage.
