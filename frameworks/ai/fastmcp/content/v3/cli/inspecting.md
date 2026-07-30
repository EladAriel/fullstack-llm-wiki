---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/v3/cli/inspecting.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.582785Z"
---
---
title: Inspecting Servers
sidebarTitle: Inspecting
description: View a server's components and metadata
icon: magnifying-glass
---

import { VersionBadge } from '/snippets/version-badge.mdx'

<VersionBadge version="2.9.0" />

`fastmcp inspect` loads a server and reports what it contains — its tools, resources, prompts, version, and metadata. The default output is a human-readable summary:

```bash
fastmcp inspect server.py
```

```
Server: MyServer
Instructions: A helpful MCP server
Version: 1.0.0

Components:
  Tools: 5
  Prompts: 2
  Resources: 3
  Templates: 1

Environment:
  FastMCP: 2.0.0
  MCP: 1.0.0

Use --format [fastmcp|mcp] for complete JSON output
```

## JSON Output

For programmatic use, two JSON formats are available:

**FastMCP format** (`--format fastmcp`) includes everything FastMCP knows about the server — tool tags, enabled status, output schemas, annotations, and custom metadata. Field names use `snake_case`. This is the format for debugging and introspecting FastMCP servers.

**MCP protocol format** (`--format mcp`) shows exactly what MCP clients see through the protocol — only standard MCP fields, `camelCase` names, no FastMCP-specific extensions. This is the format for verifying client compatibility and debugging what clients actually receive.

```bash
# Full FastMCP metadata to stdout
fastmcp inspect server.py --format fastmcp

# MCP protocol view saved to file
fastmcp inspect server.py --format mcp -o manifest.json
```

## Options

| Option | Flag | Description |
| ------ | ---- | ----------- |
| Format | `--format`, `-f` | `fastmcp` or `mcp` (required when using `-o`) |
| Output File | `--output`, `-o` | Save to file instead of stdout |

## Entrypoints

The `inspect` command supports the same local entrypoints as [`fastmcp run`](/cli/running): inferred instances, explicit entrypoints, factory functions, and `fastmcp.json` configs.

```bash
fastmcp inspect server.py                  # inferred instance
fastmcp inspect server.py:my_server        # explicit entrypoint
fastmcp inspect server.py:create_server    # factory function
fastmcp inspect fastmcp.json               # config file
```

<Warning>
`inspect` only works with local files and `fastmcp.json` — it doesn't connect to remote URLs or standard MCP config files.
</Warning>
