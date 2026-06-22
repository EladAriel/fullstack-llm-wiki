---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/faq/installation.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# Installation

## I'm getting an error about greenlet not being installed when I try to use asyncio

The `greenlet` dependency is not install by default in the 2.1 series. To install including `greenlet`, you need to add the `asyncio` [setuptools extra](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-setuptools-extras) to the `pip install` command:

```text
 pip install sqlalchemy[asyncio]
```

For more background, see `asyncio_install`.

> **Seealso:**  `asyncio_install`
