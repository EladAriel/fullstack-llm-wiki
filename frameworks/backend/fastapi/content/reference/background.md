---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/reference/background.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.718299Z"
---
# Background Tasks - `BackgroundTasks`

You can declare a parameter in a *path operation function* or dependency function with the type `BackgroundTasks`, and then you can use it to schedule the execution of background tasks after the response is sent.

You can import it directly from `fastapi`:

```python
from fastapi import BackgroundTasks
```

::: fastapi.BackgroundTasks
