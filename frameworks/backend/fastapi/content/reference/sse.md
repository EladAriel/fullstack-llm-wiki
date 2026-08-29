---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/reference/sse.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.719306Z"
---
# Server-Sent Events - `EventSourceResponse` and `ServerSentEvent`

To stream Server-Sent Events (SSE), use `yield` in your *path operation function* and set `response_class=EventSourceResponse`.

If you need to set SSE fields like `event`, `id`, `retry`, or `comment`, you can `yield` `ServerSentEvent` objects instead of plain data.

Read more about it in the [FastAPI docs for Server-Sent Events (SSE)](https://fastapi.tiangolo.com/tutorial/server-sent-events/).

You can import them directly from `fastapi.sse`:

```python
from fastapi.sse import EventSourceResponse, ServerSentEvent
```

::: fastapi.sse.EventSourceResponse

::: fastapi.sse.ServerSentEvent
