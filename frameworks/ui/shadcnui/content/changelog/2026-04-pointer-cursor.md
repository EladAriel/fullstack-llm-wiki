---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-04-pointer-cursor.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

---
title: April 2026 - Pointer Cursor
description: Add cursor pointer behavior for buttons during project setup.
date: 2026-04-25
---

You can now enable `cursor: pointer` for buttons when initializing a project.

```bash
npx shadcn@latest init --pointer
```

This adds the following CSS to your global CSS file:

```css title="globals.css"
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

The `--pointer` option is not part of preset codes. It is applied as a project setup option, similar to `--rtl`.
