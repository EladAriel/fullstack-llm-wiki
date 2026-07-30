---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-uv.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.544678Z"
---
---
title: uv
sidebarTitle: uv
---

# `fastmcp.utilities.mcp_server_config.v1.environments.uv`

## Classes

### `UVEnvironment` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mcp_server_config/v1/environments/uv.py#L14" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


Configuration for Python environment setup.


**Methods:**

#### `build_command` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mcp_server_config/v1/environments/uv.py#L49" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
build_command(self, command: list[str]) -> list[str]
```

Build complete uv run command with environment args and command to execute.

**Args:**
- `command`: Command to execute (e.g., ["fastmcp", "run", "server.py"])

**Returns:**
- Complete command ready for subprocess.run, including "uv" prefix if needed.
- If no environment configuration is set, returns the command unchanged.


#### `prepare` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mcp_server_config/v1/environments/uv.py#L109" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
prepare(self, output_dir: Path | None = None) -> None
```

Prepare the Python environment using uv.

**Args:**
- `output_dir`: Directory where the persistent uv project will be created.
       If None, creates a temporary directory for ephemeral use.

