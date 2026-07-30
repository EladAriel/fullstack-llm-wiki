---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-types.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.538777Z"
---
---
title: types
sidebarTitle: types
---

# `fastmcp.types`


Reusable type annotations for FastMCP tool parameters.

These types can be used in tool function signatures to influence how
parameters are presented in UIs (e.g. `fastmcp dev apps`) and
serialized in JSON Schema.

Example:

```python
from fastmcp import FastMCP
from fastmcp.types import Textarea

mcp = FastMCP("demo")

@mcp.tool()
def run_query(sql: Textarea) -> str:
    ...
```

