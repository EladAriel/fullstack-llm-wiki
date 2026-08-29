---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-04-component-composition.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.958974Z"
---
# 2026 04 Component Composition

---
title: April 2026 - Component Composition
description: Composition sections across component pages—structured trees that help you and your agents build correct UI.
date: 2026-04-06
---

We've added **Composition** sections across the component docs so you can see the correct structure at a glance: what wraps what, which subcomponents belong together, and how to avoid invalid nesting.

```text
Card
├── CardHeader
│   ├── CardTitle
│   ├── CardDescription
│   └── CardAction
├── CardContent
└── CardFooter
```

## Why we added this

We've found that **LLMs and coding agents compose elements more reliably** when they can see the full structure: fewer missing wrappers, fewer wrong hierarchies, better matches to the examples.

### Bring docs into your agent

You or your LLM can pull the same component documentation, including composition, usage, and examples, into context from the CLI:

```bash
npx shadcn@latest docs card
```

If you're using the [shadcn/skills](/docs/skills), this is done automatically for you.
