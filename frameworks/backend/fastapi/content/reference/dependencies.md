---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/reference/dependencies.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.720566Z"
---
# Dependencies - `Depends()` and `Security()`

## `Depends()`

Dependencies are handled mainly with the special function `Depends()` that takes a callable.

Here is the reference for it and its parameters.

You can import it directly from `fastapi`:

```python
from fastapi import Depends
```

::: fastapi.Depends

## `Security()`

For many scenarios, you can handle security (authorization, authentication, etc.) with dependencies, using `Depends()`.

But when you want to also declare OAuth2 scopes, you can use `Security()` instead of `Depends()`.

You can import `Security()` directly from `fastapi`:

```python
from fastapi import Security
```

::: fastapi.Security
