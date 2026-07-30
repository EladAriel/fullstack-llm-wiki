---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-cli.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.539507Z"
---
---
title: cli
sidebarTitle: cli
---

# `fastmcp.utilities.cli`

## Functions

### `is_already_in_uv_subprocess` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/cli.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
is_already_in_uv_subprocess() -> bool
```


Check if we're already running in a FastMCP uv subprocess.


### `load_and_merge_config` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/cli.py#L33" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
load_and_merge_config(server_spec: str | None, **cli_overrides) -> tuple[MCPServerConfig, str]
```


Load config from server_spec and apply CLI overrides.

This consolidates the config parsing logic that was duplicated across
run, inspect, and dev commands.

**Args:**
- `server_spec`: Python file, config file, URL, or None to auto-detect
- `cli_overrides`: CLI arguments that override config values

**Returns:**
- Tuple of (MCPServerConfig, resolved_server_spec)


### `log_server_banner` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/cli.py#L201" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
log_server_banner(server: FastMCP[Any]) -> None
```


Creates and logs a formatted banner with server information and logo.

