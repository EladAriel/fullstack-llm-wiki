---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/aria/toggle-group.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.970349Z"
---
# Toggle Group

---
title: Toggle Group
description: A set of two-state buttons that can be toggled on or off.
base: aria
component: true
links:
  doc: https://react-aria.adobe.com/ToggleButtonGroup
  api: https://react-aria.adobe.com/ToggleButtonGroup#api
---

<ComponentPreview styleName="aria-nova" name="toggle-group-demo" />

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
npm install react-aria-components
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="toggle-group"
  title="components/ui/toggle-group.tsx"
  styleName="aria-nova"
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
<ToggleGroup selectionMode="single">
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

## Outline

Use `variant="outline"` for an outline style.

<ComponentPreview styleName="aria-nova" name="toggle-group-outline" />

## Size

Use the `size` prop to change the size of the toggle group.

<ComponentPreview styleName="aria-nova" name="toggle-group-sizes" />

## Spacing

Use `spacing` to add spacing between toggle group items.

<ComponentPreview styleName="aria-nova" name="toggle-group-spacing" />

## Vertical

Use `orientation="vertical"` for vertical toggle groups.

<ComponentPreview styleName="aria-nova" name="toggle-group-vertical" />

## Disabled

<ComponentPreview styleName="aria-nova" name="toggle-group-disabled" />

## Custom

A custom toggle group example.

<ComponentPreview
  styleName="aria-nova"
  name="toggle-group-font-weight-selector"
  previewClassName="*:data-[slot=field]:max-w-xs"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="aria-nova"
  name="toggle-group-rtl"
  direction="rtl"
/>

## API Reference

See the [React Aria ToggleButtonGroup](https://react-aria.adobe.com/ToggleButtonGroup#api) documentation.
