---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/v3/servers/transforms/namespace.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.603542Z"
---
---
title: Namespace Transform
sidebarTitle: Namespace
description: Prefix component names to prevent conflicts
icon: tag
---

import { VersionBadge } from '/snippets/version-badge.mdx'

<VersionBadge version="3.0.0" />

The `Namespace` transform prefixes all component names, preventing conflicts when composing multiple servers.

Tools and prompts receive an underscore-separated prefix. Resources and templates receive a path-segment prefix in their URIs.

| Component | Original | With `Namespace("api")` |
|-----------|----------|-------------------------|
| Tool | `my_tool` | `api_my_tool` |
| Prompt | `my_prompt` | `api_my_prompt` |
| Resource | `data://info` | `data://api/info` |
| Template | `data://{id}` | `data://api/{id}` |

The most common use is through the `mount()` method's `namespace` parameter.

```python
from fastmcp import FastMCP

weather = FastMCP("Weather")
calendar = FastMCP("Calendar")

@weather.tool
def get_data() -> str:
    return "Weather data"

@calendar.tool
def get_data() -> str:
    return "Calendar data"

# Without namespacing, these would conflict
main = FastMCP("Main")
main.mount(weather, namespace="weather")
main.mount(calendar, namespace="calendar")

# Clients see: weather_get_data, calendar_get_data
```

You can also apply namespacing directly using the `Namespace` transform.

```python
from fastmcp import FastMCP
from fastmcp.server.transforms import Namespace

mcp = FastMCP("Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Namespace all components
mcp.add_transform(Namespace("api"))

# Tool is now: api_greet
```
