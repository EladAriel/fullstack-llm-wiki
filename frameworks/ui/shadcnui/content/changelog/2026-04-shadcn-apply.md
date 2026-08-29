---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-04-shadcn-apply.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.960042Z"
---
# 2026 04 Shadcn Apply

---
title: April 2026 - shadcn apply
description: Switch presets in existing projects without starting over.
date: 2026-04-08
---

We added `shadcn apply` so you can switch presets in an existing project without starting over.

When you run `npx shadcn@latest apply` in an existing project, we apply a new preset, reinstall your existing components, and update your theme, colors, CSS variables, fonts, and icons.

```bash
npx shadcn@latest apply --preset b2D0vQ7G4
```

The CLI keeps the current base and RTL settings from your existing project, even when the preset URL was generated with different values.

<Button asChild size="sm">
  <Link href="/create" className="mt-6 no-underline!">
    Try a Preset
  </Link>
</Button>
