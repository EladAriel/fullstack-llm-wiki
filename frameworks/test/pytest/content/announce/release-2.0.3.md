---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.0.3.rst"
source_commit: "fdba12e1708313f56e9cf713d260c029764ca2b7"
source_commit_short: "fdba12e"
source_commit_date: "2026-08-27T21:55:50+02:00"
generated_at: "2026-08-29T09:40:11.184521Z"
---
# py.test 2.0.3: bug fixes and speed ups

Welcome to pytest-2.0.3, a maintenance and bug fix release of pytest,
a mature testing tool for Python, supporting CPython 2.4-3.2, Jython
and latest PyPy interpreters.  See the extensive docs with tested examples here:

    http://pytest.org/

If you want to install or upgrade pytest, just type one of::

    pip install -U pytest # or
    easy_install -U pytest

There also is a bugfix release 1.6 of pytest-xdist, the plugin
that enables seamless distributed and "looponfail" testing for Python.

best,
holger krekel

## Changes between 2.0.2 and 2.0.3

- fix issue38: nicer tracebacks on calls to hooks, particularly early
  configure/sessionstart ones

- fix missing skip reason/meta information in junitxml files, reported
  via http://lists.idyll.org/pipermail/testing-in-python/2011-March/003928.html

- fix issue34: avoid collection failure with "test" prefixed classes
  deriving from object.

- don't require zlib (and other libs) for genscript plugin without
  --genscript actually being used.

- speed up skips (by not doing a full traceback representation
  internally)

- fix issue37: avoid invalid characters in junitxml's output