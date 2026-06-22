---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/yieldfixture.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

:orphan:

## "yield_fixture" functions

> **Important:**  Since pytest-3.0, fixtures using the normal `fixture` decorator can use a `yield`
 statement to provide fixture values and execute teardown code, exactly like `yield_fixture`
 in previous versions.
 Marking functions as `yield_fixture` is still supported, but deprecated and should not
 be used in new code.
