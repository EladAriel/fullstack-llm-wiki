---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2023-07-javascript.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: July 2023 - JavaScript
description: JavaScript version of components available via the CLI.
date: 2023-07-04
---

This project and the components are written in TypeScript. **We recommend using TypeScript for your project as well**.

However we provide a JavaScript version of the components, available via the [cli](/docs/cli).

```txt
Would you like to use TypeScript (recommended)? no
```

To opt-out of TypeScript, you can use the `tsx` flag in your `components.json` file.

```json {10} title="components.json" showLineNumbers
{
  "style": "default",
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "rsc": false,
  "tsx": false,
  "aliases": {
    "utils": "~/lib/utils",
    "components": "~/components"
  }
}
```

To configure import aliases, you can use the following `jsconfig.json`:

```json {4} title="jsconfig.json" showLineNumbers
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```
