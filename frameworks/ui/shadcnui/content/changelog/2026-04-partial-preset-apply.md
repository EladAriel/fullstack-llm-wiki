---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-04-partial-preset-apply.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.959441Z"
---
---
title: April 2026 - Partial Preset Apply
description: Apply only the theme or fonts from a preset while keeping your existing components.
date: 2026-04-22
---

You can now selectively apply a preset.

Say someone shares a preset with you and you already have your own components, but you like the theme or the fonts. Now you can apply just that.

Keep your components. Apply only what you want.

```bash
# Apply the full preset.
npx shadcn@latest apply --preset b2D0vQ7G4

# Apply only the theme.
npx shadcn@latest apply --preset b2D0vQ7G4 --only theme

# Apply only the fonts.
npx shadcn@latest apply --preset b2D0vQ7G4 --only font

# Apply theme and fonts.
npx shadcn@latest apply --preset b2D0vQ7G4 --only theme,font
```

The default behavior is unchanged. Running `shadcn apply --preset <preset>` still applies the full preset.

Partial preset apply currently supports `theme` and `font`.

<Button asChild size="sm">
  <Link href="/create" className="mt-6 no-underline!">
    Try a Preset
  </Link>
</Button>
