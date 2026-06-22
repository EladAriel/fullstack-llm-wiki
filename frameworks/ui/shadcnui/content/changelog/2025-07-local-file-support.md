---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2025-07-local-file-support.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: July 2025 - Local File Support
description: Initialize projects and add components from local JSON files.
date: 2025-07-07
---

The shadcn CLI now supports local files. Initialize projects and add components, themes, hooks, utils and more from local JSON files.

```bash
# Initialize a project from a local file
npx shadcn init ./template.json

# Add a component from a local file
npx shadcn add ./block.json
```

This feature enables powerful new workflows:

- **Zero setup** - No remote registries required
- **Faster development** - Test registry items locally before publishing
- **Enhanced workflow for agents and MCP** - Generate and run registry items locally
- **Private components** - Keep proprietary components local and private.
