---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2025-06-radix-ui.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: June 2025 - radix-ui Migration
description: A new command to migrate to the new radix-ui package.
date: 2025-06-11
---

We've added a new command to migrate to the new `radix-ui` package. This command will replace all `@radix-ui/react-*` imports with `radix-ui`.

```bash
npx shadcn@latest migrate radix
```

It will automatically update all imports in your `ui` components and install `radix-ui` as a dependency.

```diff showLineNumbers title="components/ui/alert-dialog.tsx"
- import * as AlertDialogPrimitive from "@radix-ui/react-alert-dialog"
+ import { AlertDialog as AlertDialogPrimitive } from "radix-ui"
```

Make sure to test your components and project after running the command.

**Note:** To update imports for newly added components, run the migration command again.
