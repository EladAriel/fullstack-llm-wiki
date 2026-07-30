---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-timeout.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.541641Z"
---
---
title: timeout
sidebarTitle: timeout
---

# `fastmcp.utilities.timeout`


Timeout normalization utilities.

## Functions

### `normalize_timeout_to_timedelta` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/timeout.py#L8" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
normalize_timeout_to_timedelta(value: int | float | datetime.timedelta | None) -> datetime.timedelta | None
```


Normalize a timeout value to a timedelta.

**Args:**
- `value`: Timeout value as int/float (seconds), timedelta, or None

**Returns:**
- timedelta if value provided, None otherwise


### `normalize_timeout_to_seconds` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/timeout.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
normalize_timeout_to_seconds(value: int | float | datetime.timedelta | None) -> float | None
```


Normalize a timeout value to seconds (float).

**Args:**
- `value`: Timeout value as int/float (seconds), timedelta, or None.
Zero values are treated as "disabled" and return None.

**Returns:**
- float seconds if value provided and non-zero, None otherwise

