---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/reference/parameters.md"
source_commit: "255b912928904e3ba5980425a54d6837c8bd1a1c"
source_commit_short: "255b9129"
source_commit_date: "2026-07-24T21:15:37Z"
generated_at: "2026-07-25T11:50:10Z"
---

# Request Parameters

Here's the reference information for the request parameters.

These are the special functions that you can put in *path operation function* parameters or dependency functions with `Annotated` to get data from the request.

It includes:

* `Query()`
* `Path()`
* `Body()`
* `Cookie()`
* `Header()`
* `Form()`
* `File()`

You can import them all directly from `fastapi`:

```python
from fastapi import Body, Cookie, File, Form, Header, Path, Query
```

::: fastapi.Query

::: fastapi.Path

::: fastapi.Body

::: fastapi.Cookie

::: fastapi.Header

::: fastapi.Form

::: fastapi.File
