---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/reference/response.md"
source_commit: "255b912928904e3ba5980425a54d6837c8bd1a1c"
source_commit_short: "255b9129"
source_commit_date: "2026-07-24T21:15:37Z"
generated_at: "2026-07-25T11:50:10Z"
---

# `Response` class

You can declare a parameter in a *path operation function* or dependency to be of type `Response` and then you can set data for the response like headers or cookies.

You can also use it directly to create an instance of it and return it from your *path operations*.

Read more about it in the [FastAPI docs about returning a custom Response](https://fastapi.tiangolo.com/advanced/response-directly/#returning-a-custom-response)

You can import it directly from `fastapi`:

```python
from fastapi import Response
```

::: fastapi.Response
