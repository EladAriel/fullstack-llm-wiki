---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-filesystem.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.539346Z"
---
---
title: filesystem
sidebarTitle: filesystem
---

# `fastmcp.utilities.mcp_server_config.v1.sources.filesystem`

## Classes

### `FileSystemSource` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mcp_server_config/v1/sources/filesystem.py#L16" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Source for local Python files.


**Methods:**

#### `parse_path_with_object` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mcp_server_config/v1/sources/filesystem.py#L29" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
parse_path_with_object(cls, v: str) -> str
```

Parse path:object syntax and extract the object name.

This validator runs before the model is created, allowing us to
handle the "file.py:object" syntax at the model boundary.


#### `load_server` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mcp_server_config/v1/sources/filesystem.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
load_server(self) -> Any
```

Load server from filesystem.

