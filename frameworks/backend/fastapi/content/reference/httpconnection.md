---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/reference/httpconnection.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.719163Z"
---
# `HTTPConnection` class

When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an `HTTPConnection` instead of a `Request` or a `WebSocket`.

You can import it from `fastapi.requests`:

```python
from fastapi.requests import HTTPConnection
```

::: fastapi.requests.HTTPConnection
