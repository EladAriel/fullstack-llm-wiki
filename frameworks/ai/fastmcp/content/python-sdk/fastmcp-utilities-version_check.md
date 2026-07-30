---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-version_check.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.546931Z"
---
---
title: version_check
sidebarTitle: version_check
---

# `fastmcp.utilities.version_check`


Version checking utilities for FastMCP.

## Functions

### `get_latest_version` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/version_check.py#L98" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_latest_version(include_prereleases: bool = False) -> str | None
```


Get the latest version of FastMCP from PyPI, using cache when available.

**Args:**
- `include_prereleases`: If True, include pre-release versions.

**Returns:**
- The latest version string, or None if unavailable.


### `check_for_newer_version` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/version_check.py#L124" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
check_for_newer_version() -> str | None
```


Check if a newer version of FastMCP is available.

**Returns:**
- The latest version string if newer than current, None otherwise.

