---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/clients/progress.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.567781Z"
---
# Progress

---
title: Progress Monitoring
sidebarTitle: Progress
description: Handle progress notifications from long-running server operations.
icon: bars-progress
---

import { VersionBadge } from '/snippets/version-badge.mdx'

<VersionBadge version="2.3.5" />

Use this when you need to track progress of long-running operations.

MCP servers can report progress during operations. The client receives these updates through a progress handler.

## Progress Handler

Set a handler when creating the client:

```python
from fastmcp import Client

async def progress_handler(
    progress: float,
    total: float | None,
    message: str | None
) -> None:
    if total is not None:
        percentage = (progress / total) * 100
        print(f"Progress: {percentage:.1f}% - {message or ''}")
    else:
        print(f"Progress: {progress} - {message or ''}")

client = Client(
    "my_mcp_server.py",
    progress_handler=progress_handler
)
```

The handler receives three parameters:

<Card icon="code" title="Handler Parameters">
<ResponseField name="progress" type="float">
  Current progress value
</ResponseField>

<ResponseField name="total" type="float | None">
  Expected total value (may be None if unknown)
</ResponseField>

<ResponseField name="message" type="str | None">
  Optional status message
</ResponseField>
</Card>

## Per-Call Handler

Override the client-level handler for specific tool calls:

```python
async with client:
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        progress_handler=my_progress_handler
    )
```
