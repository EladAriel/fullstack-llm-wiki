---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/toggle.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Toggle
description: A two-state button that can be either on or off.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/toggle
  api: https://www.radix-ui.com/docs/primitives/components/toggle#api-reference
---

<ComponentPreview styleName="radix-nova" name="toggle-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add toggle
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
  name="toggle"
  title="components/ui/toggle.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Toggle } from "@/components/ui/toggle"
```

```tsx
<Toggle>Toggle</Toggle>
```

## Examples

### Outline

Use `variant="outline"` for an outline style.

<ComponentPreview styleName="radix-nova" name="toggle-outline" />

### With Text

<ComponentPreview styleName="radix-nova" name="toggle-text" />

### Size

Use the `size` prop to change the size of the toggle.

<ComponentPreview styleName="radix-nova" name="toggle-sizes" />

### Disabled

<ComponentPreview styleName="radix-nova" name="toggle-disabled" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="toggle-rtl" direction="rtl" />

## API Reference

See the [Radix Toggle](https://www.radix-ui.com/docs/primitives/components/toggle#api-reference) documentation.
