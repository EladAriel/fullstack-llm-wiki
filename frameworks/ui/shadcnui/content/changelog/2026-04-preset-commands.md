---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-04-preset-commands.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: April 2026 - shadcn preset
description: Decode, share, open, and resolve preset codes from the shadcn CLI.
date: 2026-04-28
---

We added `shadcn preset` commands for working with preset codes.

## Decode a preset

You can decode a preset code to see exactly what it contains:

```bash
npx shadcn@latest preset decode b5owWMfJ8l
```

```txt
Preset
  code         b5owWMfJ8l
  version      b
  style        mira
  baseColor    mauve
  theme        mauve
  chartColor   amber
  iconLibrary  hugeicons
  font         inter
  fontHeading  oxanium
  radius       large
  menuAccent   subtle
  menuColor    inverted-translucent
  url          https://ui.shadcn.com/create?preset=b5owWMfJ8l
```

## Resolve from a project

Use `preset resolve` in an existing project to see the preset that matches your current configuration.

```bash
npx shadcn@latest preset resolve
```

```txt
Preset
  code         b5Kc6P0Vc
  version      b
  style        luma
  baseColor    olive
  theme        lime
  chartColor   sky
  iconLibrary  hugeicons
  font         geist
  fontHeading  inherit
  radius       default
  menuAccent   subtle
  menuColor    default
  url          https://ui.shadcn.com/create?preset=b5Kc6P0Vc
```

It works with monorepos too:

```bash
npx shadcn@latest preset resolve -c apps/web
```

## Share or open

Use `preset url` when you need a shareable link:

```bash
npx shadcn@latest preset url b5owWMfJ8l
```

```txt
https://ui.shadcn.com/create?preset=b5owWMfJ8l
```

Use `preset open` to open the preset on shadcn/create for customization:

```bash
npx shadcn@latest preset open b5owWMfJ8l
```

```txt
Opening https://ui.shadcn.com/create?preset=b5owWMfJ8l in your browser.
```

This makes presets easier to inspect, share, and hand off to coding agents without manually decoding codes or building URLs.

<Button asChild size="sm">
  <Link href="/create" className="mt-6 no-underline!">
    Try a Preset
  </Link>
</Button>
