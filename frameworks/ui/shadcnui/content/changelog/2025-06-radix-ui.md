---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2025-06-radix-ui.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.956919Z"
---
# 2025 06 Radix Ui

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
