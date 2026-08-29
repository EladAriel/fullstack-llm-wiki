---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/yieldfixture.rst"
source_commit: "fdba12e1708313f56e9cf713d260c029764ca2b7"
source_commit_short: "fdba12e"
source_commit_date: "2026-08-27T21:55:50+02:00"
generated_at: "2026-08-29T09:40:11.172252Z"
---
# Yieldfixture

:orphan:

.. _yieldfixture:

## "yield_fixture" functions





**important:** Since pytest-3.0, fixtures using the normal ``fixture`` decorator can use a ``yield``
    statement to provide fixture values and execute teardown code, exactly like ``yield_fixture``
    in previous versions.

    Marking functions as ``yield_fixture`` is still supported, but deprecated and should not
    be used in new code.