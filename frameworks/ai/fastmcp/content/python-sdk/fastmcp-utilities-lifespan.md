---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-lifespan.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.546241Z"
---
---
title: lifespan
sidebarTitle: lifespan
---

# `fastmcp.utilities.lifespan`


Lifespan utilities for combining async context manager lifespans.

## Functions

### `combine_lifespans` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/lifespan.py#L12" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
combine_lifespans(*lifespans: Callable[[AppT], AbstractAsyncContextManager[Mapping[str, Any] | None]]) -> Callable[[AppT], AbstractAsyncContextManager[dict[str, Any]]]
```


Combine multiple lifespans into a single lifespan.

Useful when mounting FastMCP into FastAPI and you need to run
both your app's lifespan and the MCP server's lifespan.

Works with both FastAPI-style lifespans (yield None) and FastMCP-style
lifespans (yield dict). Results are merged; later lifespans override
earlier ones on key conflicts.

Lifespans are entered in order and exited in reverse order (LIFO).

**Args:**
- `*lifespans`: Lifespan context manager factories to combine.

**Returns:**
- A combined lifespan context manager factory.

