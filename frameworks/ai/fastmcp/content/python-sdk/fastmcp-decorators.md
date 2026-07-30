---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-decorators.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.543495Z"
---
---
title: decorators
sidebarTitle: decorators
---

# `fastmcp.decorators`


Shared decorator utilities for FastMCP.

## Functions

### `resolve_task_config` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/decorators.py#L17" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
resolve_task_config(task: bool | TaskConfig | None) -> bool | TaskConfig
```


Resolve task config, defaulting None to False.


### `get_fastmcp_meta` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/decorators.py#L29" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_fastmcp_meta(fn: Any) -> Any | None
```


Extract FastMCP metadata from a function, handling bound methods and wrappers.


## Classes

### `HasFastMCPMeta` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/decorators.py#L23" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Protocol for callables decorated with FastMCP metadata.

