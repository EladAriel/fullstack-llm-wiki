---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/reference/request.md"
source_commit: "255b912928904e3ba5980425a54d6837c8bd1a1c"
source_commit_short: "255b9129"
source_commit_date: "2026-07-24T21:15:37Z"
generated_at: "2026-07-25T11:50:10Z"
---

# `Request` class

You can declare a parameter in a *path operation function* or dependency to be of type `Request` and then you can access the raw request object directly, without any validation, etc.

Read more about it in the [FastAPI docs about using Request directly](https://fastapi.tiangolo.com/advanced/using-request-directly/)

You can import it directly from `fastapi`:

```python
from fastapi import Request
```

/// tip

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.

///

::: fastapi.Request
