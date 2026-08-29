---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-04-pointer-cursor.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.963707Z"
---
# 2026 04 Pointer Cursor

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
