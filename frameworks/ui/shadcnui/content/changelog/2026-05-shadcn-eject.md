---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-05-shadcn-eject.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: May 2026 - shadcn eject
description: Inline shadcn/tailwind.css and remove the shadcn dependency.
date: 2026-05-31
---

When we added support for both Radix and Base UI, we needed a place for shared Tailwind utilities that both libraries depend on, e.g. custom variants like `data-open:` and `data-closed:` and utilities like `no-scrollbar`.

We also ran into a few bugs while working on RTL support that were easier to fix in one shared place rather than duplicating across every component.

So we created `shadcn/tailwind.css`. When you run `init`, it adds `@import "shadcn/tailwind.css"` to your global CSS file. It works just like other CSS imports such as `tw-animate-css`: a small dependency that is tree-shaken in production and resolved at build time.

If you prefer not to depend on the `shadcn` package for that CSS, we've added the `shadcn eject` command. It inlines `shadcn/tailwind.css` into your global CSS file and removes the `shadcn` dependency from your project.

```bash
npx shadcn@latest eject
```

**Before**

```css
@import "tailwindcss";
@import "tw-animate-css";
@import "shadcn/tailwind.css";
```

**After**

```css
@import "tailwindcss";
@import "tw-animate-css";
/* ejected from shadcn@4.8.3 */
@theme inline {
  @keyframes accordion-down {
    from {
      height: 0;
    }
    to {
      height: var(
        --radix-accordion-content-height,
        var(--accordion-panel-height, auto)
      );
    }
  }
}

@custom-variant data-open {
  &:where([data-state="open"]),
  &:where([data-open]:not([data-open="false"])) {
    @slot;
  }
}
```

In a monorepo, run the command from the workspace that contains your `components.json` and global CSS file:

```bash
npx shadcn@latest eject -c packages/ui
```

See the [CLI documentation](/docs/cli#eject) for more details.
