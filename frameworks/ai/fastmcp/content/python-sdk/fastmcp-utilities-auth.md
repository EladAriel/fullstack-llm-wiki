---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-auth.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.541302Z"
---
---
title: auth
sidebarTitle: auth
---

# `fastmcp.utilities.auth`


Authentication utility helpers.

## Functions

### `decode_jwt_header` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/auth.py#L32" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
decode_jwt_header(token: str) -> dict[str, Any]
```


Decode JWT header without signature verification.

Useful for extracting the key ID (kid) for JWKS lookup.

**Args:**
- `token`: JWT token string (header.payload.signature)

**Returns:**
- Decoded header as a dictionary

**Raises:**
- `ValueError`: If token is not a valid JWT format


### `decode_jwt_payload` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/auth.py#L49" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
decode_jwt_payload(token: str) -> dict[str, Any]
```


Decode JWT payload without signature verification.

Use only for tokens received directly from trusted sources (e.g., IdP token endpoints).

**Args:**
- `token`: JWT token string (header.payload.signature)

**Returns:**
- Decoded payload as a dictionary

**Raises:**
- `ValueError`: If token is not a valid JWT format


### `parse_scopes` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/auth.py#L66" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
parse_scopes(value: Any) -> list[str] | None
```


Parse scopes from environment variables or settings values.

Accepts either a JSON array string, a comma- or space-separated string,
a list of strings, or ``None``. Returns a list of scopes or ``None`` if
no value is provided.

