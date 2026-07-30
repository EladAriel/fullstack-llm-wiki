---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-settings.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.540987Z"
---
---
title: settings
sidebarTitle: settings
---

# `fastmcp.settings`

## Classes

### `Settings` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/settings.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


FastMCP settings.


**Methods:**

#### `get_setting` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/settings.py#L44" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_setting(self, attr: str) -> Any
```

Get a setting. If the setting contains one or more `__`, it will be
treated as a nested setting.


#### `set_setting` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/settings.py#L57" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
set_setting(self, attr: str, value: Any) -> None
```

Set a setting. If the setting contains one or more `__`, it will be
treated as a nested setting.


#### `normalize_log_level` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/settings.py#L79" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
normalize_log_level(cls, v)
```
