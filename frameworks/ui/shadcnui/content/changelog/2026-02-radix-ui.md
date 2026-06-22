---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-02-radix-ui.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: February 2026 - Unified Radix UI Package
description: The new-york style now uses the unified radix-ui package.
date: 2026-02-02
---

The `new-york` style now uses the unified `radix-ui` package instead of individual `@radix-ui/react-*` packages.

### What's Changed

When you add components using the `new-york` style, they will now import from `radix-ui` instead of separate packages:

```diff title="components/ui/dialog.tsx"
- import * as DialogPrimitive from "@radix-ui/react-dialog"
+ import { Dialog as DialogPrimitive } from "radix-ui"
```

This results in a cleaner `package.json` with a single `radix-ui` dependency instead of multiple `@radix-ui/react-*` packages.

### Migrating Existing Projects

If you have an existing project using the `new-york` style, you can migrate to the new `radix-ui` package using the migrate command:

```bash
npx shadcn@latest migrate radix
```

This will update all imports in your UI components and add `radix-ui` to your dependencies.

To migrate components outside of your `ui` directory, use the `path` argument:

```bash
npx shadcn@latest migrate radix src/components/custom
```

Once complete, you can remove any unused `@radix-ui/react-*` packages from your `package.json`.

See the [migrate radix documentation](/docs/cli#migrate-radix) for more details.
