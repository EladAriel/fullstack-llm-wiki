---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-05-package-imports-target-aliases.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: May 2026 - Package Imports and Target Aliases
description: Configure shadcn/ui with package.json imports and portable registry target aliases.
date: 2026-05-05
---

We've added support for package imports and aliases in `files.target` in `shadcn@4.7.0`.

## Package imports

The `shadcn` CLI now supports `package.json#imports` for installing components,
rewriting imports, and resolving third-party registries. You can use private
`#...` import aliases from your `package.json` instead of relying only on
`compilerOptions.paths` in `tsconfig.json`.

```json title="package.json" showLineNumbers
{
  "imports": {
    "#components/*": "./src/components/*.tsx",
    "#lib/*": "./src/lib/*.ts",
    "#hooks/*": "./src/hooks/*.ts"
  }
}
```

Then use the same roots in `components.json`:

```json title="components.json" showLineNumbers
{
  "aliases": {
    "components": "#components",
    "ui": "#components/ui",
    "lib": "#lib",
    "hooks": "#hooks",
    "utils": "#lib/utils"
  }
}
```

This also works in monorepos where app-local files use package imports and
shared UI files are imported from workspace package exports.

See the [package imports guide](/docs/package-imports) for setup details.

## Target aliases

Registry items can now use target aliases in `files[].target` to install files
under the user's configured shadcn directories. For example, the following registry item will install the `prompt-input.tsx` file under the `ui/ai` directory.

```json title="example.json" showLineNumbers
{
  "files": [
    {
      "path": "registry/default/ai/prompt-input.tsx",
      "type": "registry:ui",
      "target": "@ui/ai/prompt-input.tsx"
    }
  ]
}
```

See the [registry examples](/docs/registry/examples#target-placeholders) for
more details.
