---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/slider.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Slider
description: An input where the user selects a value from within a given range.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/slider
  api: https://www.radix-ui.com/docs/primitives/components/slider#api-reference
---

<ComponentPreview styleName="radix-nova" name="slider-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add slider
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
  name="slider"
  title="components/ui/slider.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Slider } from "@/components/ui/slider"
```

```tsx
<Slider defaultValue={[33]} max={100} step={1} />
```

## Examples

### Range

Use an array with two values for a range slider.

<ComponentPreview styleName="radix-nova" name="slider-range" />

### Multiple Thumbs

Use an array with multiple values for multiple thumbs.

<ComponentPreview styleName="radix-nova" name="slider-multiple" />

### Vertical

Use `orientation="vertical"` for a vertical slider.

<ComponentPreview styleName="radix-nova" name="slider-vertical" />

### Controlled

<ComponentPreview styleName="radix-nova" name="slider-controlled" />

### Disabled

Use the `disabled` prop to disable the slider.

<ComponentPreview styleName="radix-nova" name="slider-disabled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="slider-rtl" direction="rtl" />

## API Reference

See the [Radix UI Slider](https://www.radix-ui.com/docs/primitives/components/slider#api-reference) documentation.
