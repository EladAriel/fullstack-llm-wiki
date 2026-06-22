---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/progress.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Progress
description: Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/progress
  api: https://www.radix-ui.com/docs/primitives/components/progress#api-reference
---

<ComponentPreview styleName="radix-nova" name="progress-demo" />

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
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="progress"
  title="components/ui/progress.tsx"
  styleName="radix-nova"
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

## Examples

### Label

Use a `Field` component to add a label to the progress bar.

<ComponentPreview styleName="radix-nova" name="progress-label" />

### Controlled

A progress bar that can be controlled by a slider.

<ComponentPreview styleName="radix-nova" name="progress-controlled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="progress-rtl" direction="rtl" />

## API Reference

See the [Radix UI Progress](https://www.radix-ui.com/docs/primitives/components/progress#api-reference) documentation.
