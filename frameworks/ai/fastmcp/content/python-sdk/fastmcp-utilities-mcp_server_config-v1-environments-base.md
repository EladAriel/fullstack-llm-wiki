---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-base.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.543689Z"
---
---
title: base
sidebarTitle: base
---

# `fastmcp.utilities.mcp_server_config.v1.environments.base`

## Classes

### `Environment` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mcp_server_config/v1/environments/base.py#L7" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Base class for environment configuration.


**Methods:**

#### `build_command` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mcp_server_config/v1/environments/base.py#L13" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
build_command(self, command: list[str]) -> list[str]
```

Build the full command with environment setup.

**Args:**
- `command`: Base command to wrap with environment setup

**Returns:**
- Full command ready for subprocess execution


#### `prepare` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mcp_server_config/v1/environments/base.py#L23" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
prepare(self, output_dir: Path | None = None) -> None
```

Prepare the environment (optional, can be no-op).

**Args:**
- `output_dir`: Directory for persistent environment setup

