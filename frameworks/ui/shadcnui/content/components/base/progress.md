---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/progress.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Progress
description: Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/progress
  api: https://base-ui.com/react/components/progress#api-reference
---

<ComponentPreview styleName="base-nova" name="progress-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add progress
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="progress"
  title="components/ui/progress.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Progress } from "@/components/ui/progress"
```

```tsx showLineNumbers
<Progress value={33} />
```

## Composition

### With label and value

Use `ProgressLabel` and `ProgressValue` to add a label and value display.

```tsx showLineNumbers
import {
  Progress,
  ProgressLabel,
  ProgressValue,
} from "@/components/ui/progress"

;<Progress value={56} className="w-full max-w-sm">
  <ProgressLabel>Upload progress</ProgressLabel>
  <ProgressValue />
</Progress>
```

```text
Progress
├── ProgressLabel
├── ProgressValue
└── ProgressTrack
    └── ProgressIndicator
```

## Examples

### Label

Use `ProgressLabel` and `ProgressValue` to add a label and value display.

<ComponentPreview styleName="base-nova" name="progress-label" />

### Controlled

A progress bar that can be controlled by a slider.

<ComponentPreview styleName="base-nova" name="progress-controlled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="progress-rtl" direction="rtl" />

## API Reference

See the [Base UI Progress](https://base-ui.com/react/components/progress#api-reference) documentation.
