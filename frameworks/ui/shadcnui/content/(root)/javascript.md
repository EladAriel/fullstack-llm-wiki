---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/(root)/javascript.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: JavaScript
description: How to use shadcn/ui with JavaScript
---

This project and the components are written in TypeScript. We recommend using TypeScript for your project as well.

However we provide a JavaScript version of the components as well. The JavaScript version is available via the [cli](/docs/cli).

To opt-out of TypeScript, you can use the `tsx` flag in your `components.json` file.

```json {4} title="components.json" showLineNumbers
{
  "style": "new-york",
  "rsc": false,
  "tsx": false,
  "tailwind": {
    "config": "",
    "css": "src/app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
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
