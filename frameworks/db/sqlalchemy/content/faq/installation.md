---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/faq/installation.rst"
source_commit: "aa1a5575358d3aa14953b04dced02f4763fed2e7"
source_commit_short: "aa1a5575"
source_commit_date: "2026-07-23T18:02:59Z"
generated_at: "2026-07-25T11:50:45Z"
---

# Installation

## I'm getting an error about greenlet not being installed when I try to use asyncio

The `greenlet` dependency is not install by default in the 2.1 series. To install including `greenlet`, you need to add the `asyncio` [setuptools extra](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-setuptools-extras) to the `pip install` command:

```text
 pip install sqlalchemy[asyncio]
```

For more background, see `asyncio_install`.

> **Seealso:**  `asyncio_install`
