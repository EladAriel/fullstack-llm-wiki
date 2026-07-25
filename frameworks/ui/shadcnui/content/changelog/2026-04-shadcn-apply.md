---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-04-shadcn-apply.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

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
