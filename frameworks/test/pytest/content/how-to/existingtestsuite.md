---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/how-to/existingtestsuite.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# How to use pytest with an existing test suite

Pytest can be used with most existing test suites, but its behavior differs from other test runners such as Python's default unittest framework.

Before using this section you will want to `install pytest <getstarted>`.

## Running an existing test suite with pytest

Say you want to contribute to an existing repository somewhere. After pulling the code into your development space using some flavor of version control and (optionally) setting up a virtualenv you will want to run:

```bash
 cd <repository>
 pip install -e .  # Environment dependent alternatives include
                   # 'python setup.py develop' and 'conda develop'
```

in your project root.  This will set up a symlink to your code in site-packages, allowing you to edit your code while your tests run against it as if it were installed.

Setting up your project in development mode lets you avoid having to reinstall every time you want to run your tests, and is less brittle than mucking about with sys.path to point your tests at local code.

Also consider using `tox <use tox>`.
