---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-docstring_parsing.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.542309Z"
---
---
title: docstring_parsing
sidebarTitle: docstring_parsing
---

# `fastmcp.utilities.docstring_parsing`


Extract descriptions from function docstrings.

Uses griffelib to parse Google, NumPy, and Sphinx-style docstrings. The
interface is intentionally narrow — a single function returning a
`ParsedDocstring` — so the implementation can be swapped without touching
callers.


## Functions

### `parse_docstring` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/docstring_parsing.py#L35" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
parse_docstring(fn: Callable[..., Any]) -> ParsedDocstring
```


Parse a function's docstring into a summary and parameter descriptions.

Tries Google, NumPy, and Sphinx parsers in order, using the first one that
successfully extracts parameter descriptions. If none do, returns the full
docstring as the description with no parameter descriptions.


## Classes

### `ParsedDocstring` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/docstring_parsing.py#L28" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


The extracted description and per-parameter descriptions from a docstring.

