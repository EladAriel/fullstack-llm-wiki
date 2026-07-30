---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-apps-generative.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.540667Z"
---
---
title: generative
sidebarTitle: generative
---

# `fastmcp.apps.generative`


GenerativeUI — a Provider that adds LLM-generated UI capabilities.

Registers tools and resources from ``prefab_ui.generative`` so that an
LLM can write Prefab Python code, execute it in a sandbox, and render
the result as a streaming interactive UI.

Requires ``fastmcp[apps]`` (prefab-ui).

Usage::

    from fastmcp import FastMCP
    from fastmcp.apps.generative import GenerativeUI

    mcp = FastMCP("My Server")
    mcp.add_provider(GenerativeUI())


## Classes

### `GenerativeUI` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/apps/generative.py#L53" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>


A Provider that adds generative UI capabilities to a server.

Registers:

- A ``generate_ui`` tool that accepts Prefab Python code, executes
  it in a Pyodide sandbox, and returns the rendered PrefabApp.
  Supports streaming via ``ontoolinputpartial``.
- A ``components`` tool that searches the Prefab component library.
- The generative renderer resource with CSP for Pyodide CDN access.

Example::

    from fastmcp import FastMCP
    from fastmcp.apps.generative import GenerativeUI

    mcp = FastMCP("My Server")
    mcp.add_provider(GenerativeUI())


**Methods:**

#### `lifespan` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/apps/generative.py#L196" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
lifespan(self) -> AsyncIterator[None]
```
