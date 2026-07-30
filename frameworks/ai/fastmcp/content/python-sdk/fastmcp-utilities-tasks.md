---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-tasks.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.543002Z"
---
---
title: tasks
sidebarTitle: tasks
---

# `fastmcp.utilities.tasks`


Task configuration primitives for FastMCP components.

## Classes

### `TaskMeta` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/tasks.py#L29" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Metadata for task-augmented execution requests.

**Attributes:**
- `ttl`: Client-requested TTL in milliseconds. If None, uses server default.
- `fn_key`: Docket routing key. Auto-derived from component name if None.


### `TaskConfig` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/tasks.py#L42" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Configuration for MCP background task execution.

Controls how a component handles task-augmented requests:

- ``forbidden``: Component does not support task execution.
- ``optional``: Component supports both synchronous and task execution.
- ``required``: Component requires task execution.


**Methods:**

#### `from_bool` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/tasks.py#L56" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
from_bool(cls, value: bool) -> TaskConfig
```

Convert a boolean task flag to a TaskConfig.


#### `supports_tasks` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/tasks.py#L60" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
supports_tasks(self) -> bool
```

Check if this component supports task execution.


#### `validate_function` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/tasks.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
validate_function(self, fn: Callable[..., Any], name: str) -> None
```

Validate that a function is compatible with this task config.

