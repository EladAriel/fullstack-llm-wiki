---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/v2/clients/roots.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.620610Z"
---
# Roots

---
title: Client Roots
sidebarTitle: Roots
description: Provide local context and resource boundaries to MCP servers.
icon: folder-tree
---

import { VersionBadge } from '/snippets/version-badge.mdx'

<VersionBadge version="2.0.0" />

Roots are a way for clients to inform servers about the resources they have access to. Servers can use this information to adjust behavior or provide more relevant responses.

## Setting Static Roots

Provide a list of roots when creating the client:

<CodeGroup>
```python Static Roots
from fastmcp import Client

client = Client(
    "my_mcp_server.py", 
    roots=["/path/to/root1", "/path/to/root2"]
)
```

```python Dynamic Roots Callback
from fastmcp import Client
from fastmcp.client.roots import RequestContext

async def roots_callback(context: RequestContext) -> list[str]:
    print(f"Server requested roots (Request ID: {context.request_id})")
    return ["/path/to/root1", "/path/to/root2"]

client = Client(
    "my_mcp_server.py", 
    roots=roots_callback
)
```
</CodeGroup>

