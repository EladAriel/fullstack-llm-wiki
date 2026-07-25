---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/yieldfixture.rst"
source_commit: "344c23787cdb3431dcc441b8b63ee9950f04b921"
source_commit_short: "344c2378"
source_commit_date: "2026-07-24T17:37:16+02:00"
generated_at: "2026-07-25T11:50:13Z"
---

:orphan:

## "yield_fixture" functions

> **Important:**  Since pytest-3.0, fixtures using the normal `fixture` decorator can use a `yield`
 statement to provide fixture values and execute teardown code, exactly like `yield_fixture`
 in previous versions.
 Marking functions as `yield_fixture` is still supported, but deprecated and should not
 be used in new code.
