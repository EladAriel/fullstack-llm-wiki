---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/toggle-group.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Toggle Group
description: A set of two-state buttons that can be toggled on or off.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/toggle-group
  api: https://base-ui.com/react/components/toggle-group#api-reference
---

<ComponentPreview styleName="base-nova" name="toggle-group-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add toggle-group
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
  name="toggle-group"
  title="components/ui/toggle-group.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
```

```tsx
<ToggleGroup type="single">
  <ToggleGroupItem value="a">A</ToggleGroupItem>
  <ToggleGroupItem value="b">B</ToggleGroupItem>
  <ToggleGroupItem value="c">C</ToggleGroupItem>
</ToggleGroup>
```

## Composition

Use the following composition to build a `ToggleGroup`:

```text
ToggleGroup
├── ToggleGroupItem
└── ToggleGroupItem
```

## Examples

### Outline

Use `variant="outline"` for an outline style.

<ComponentPreview styleName="base-nova" name="toggle-group-outline" />

### Size

Use the `size` prop to change the size of the toggle group.

<ComponentPreview styleName="base-nova" name="toggle-group-sizes" />

### Spacing

Use `spacing` to add spacing between toggle group items.

<ComponentPreview styleName="base-nova" name="toggle-group-spacing" />

### Vertical

Use `orientation="vertical"` for vertical toggle groups.

<ComponentPreview styleName="base-nova" name="toggle-group-vertical" />

### Disabled

<ComponentPreview styleName="base-nova" name="toggle-group-disabled" />

### Custom

A custom toggle group example.

<ComponentPreview
  styleName="base-nova"
  name="toggle-group-font-weight-selector"
  previewClassName="*:data-[slot=field]:max-w-xs"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="toggle-group-rtl"
  direction="rtl"
/>

## API Reference

See the [Base UI Toggle Group](https://base-ui.com/react/components/toggle-group#api-reference) documentation.

## Changelog

### 2026-05-17 Default Spacing

Changed the default `spacing` from `0` to `2` so toggle groups render with space between items by default. Use `spacing={0}` for connected items.
