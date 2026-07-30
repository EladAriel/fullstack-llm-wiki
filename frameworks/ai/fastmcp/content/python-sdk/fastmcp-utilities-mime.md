---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-mime.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.541969Z"
---
---
title: mime
sidebarTitle: mime
---

# `fastmcp.utilities.mime`


MIME type constants and helpers for MCP Apps UI resources.

This module has no dependencies on the server or resource packages,
so it can be safely imported from anywhere.


## Functions

### `resolve_ui_mime_type` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/mime.py#L10" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
resolve_ui_mime_type(uri: str, explicit_mime_type: str | None) -> str | None
```


Return the appropriate MIME type for a resource URI.

For ``ui://`` scheme resources, defaults to ``UI_MIME_TYPE`` when no
explicit MIME type is provided.

**Args:**
- `uri`: The resource URI string
- `explicit_mime_type`: The MIME type explicitly provided by the user

**Returns:**
- The resolved MIME type (explicit value, UI default, or None)

