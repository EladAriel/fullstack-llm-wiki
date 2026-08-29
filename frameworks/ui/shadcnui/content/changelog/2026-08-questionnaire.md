---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-08-questionnaire.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.961602Z"
---
# 2026 08 Questionnaire

---
title: August 2026 - Questionnaire
description: A new component for building multi-step question flows with fixed, freeform, multiple, and skippable answers.
date: 2026-08-05
---

Today, we're releasing [**Questionnaire**](/docs/components/base/questionnaire),
a new component for multi-step question flows. Use it for agent clarification
prompts, onboarding, surveys, intake forms, and configuration.

Questionnaire is available for Base UI, React Aria, and Radix across all eight
styles.

<ComponentPreview
  align="end"
  styleName="base-nova"
  name="questionnaire-demo"
  previewClassName="min-h-[560px] p-4 sm:p-8"
/>

## Features

- Single and multiple selection with native radios and checkboxes.
- Freeform answers alongside fixed choices.
- Explicit skipping for optional questions.
- Previous, next, submit, and custom progress controls.
- Required and custom validation.
- Controlled navigation, saved defaults, and conditional questions.
- Keyboard navigation with optional letter or number shortcuts.
- Native form serialization and server-rendered collection state.
- Standalone, Card, and Dialog composition.

## Installation

```bash
npx shadcn@latest add questionnaire
```

## @shadcn/react

The `<Questionnaire />` component is also available as an unstyled headless primitive in `@shadcn/react`. [Read the docs](/docs/react/questionnaire) to learn more.

<div className="flex flex-wrap gap-2">
  <Button asChild size="sm">
    <Link
      href="/docs/components/base/questionnaire"
      className="mt-6 no-underline!"
    >
      View Questionnaire
    </Link>
  </Button>
</div>
