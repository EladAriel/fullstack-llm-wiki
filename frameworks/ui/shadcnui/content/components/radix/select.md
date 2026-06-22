---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/select.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Select
description: Displays a list of options for the user to pick from—triggered by a button.
base: radix
component: true
featured: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/select
  api: https://www.radix-ui.com/docs/primitives/components/select#api-reference
---

<ComponentPreview styleName="radix-nova" name="select-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add select
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
  name="select"
  title="components/ui/select.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
```

```tsx showLineNumbers
<Select>
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Theme" />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      <SelectItem value="light">Light</SelectItem>
      <SelectItem value="dark">Dark</SelectItem>
      <SelectItem value="system">System</SelectItem>
    </SelectGroup>
  </SelectContent>
</Select>
```

## Composition

Use the following composition to build a `Select`:

```text
Select
├── SelectTrigger
│   └── SelectValue
└── SelectContent
    ├── SelectGroup
    │   ├── SelectLabel
    │   ├── SelectItem
    │   └── SelectItem
    ├── SelectSeparator
    └── SelectGroup
        ├── SelectLabel
        ├── SelectItem
        └── SelectItem
```

## Examples

### Align Item With Trigger

Use the `position` prop on `SelectContent` to control alignment. When `position="item-aligned"` (default), the popup positions so the selected item appears over the trigger. When `position="popper"`, the popup aligns to the trigger edge.

<ComponentPreview styleName="radix-nova" name="select-align-item" />

### Groups

Use `SelectGroup`, `SelectLabel`, and `SelectSeparator` to organize items.

<ComponentPreview styleName="radix-nova" name="select-groups" />

### Scrollable

A select with many items that scrolls.

<ComponentPreview styleName="radix-nova" name="select-scrollable" />

### Disabled

<ComponentPreview styleName="radix-nova" name="select-disabled" />

### Invalid

Add the `data-invalid` attribute to the `Field` component and the `aria-invalid` attribute to the `SelectTrigger` component to show an error state.

```tsx showLineNumbers /data-invalid/ /aria-invalid/
<Field data-invalid>
  <FieldLabel>Fruit</FieldLabel>
  <SelectTrigger aria-invalid>
    <SelectValue />
  </SelectTrigger>
</Field>
```

<ComponentPreview styleName="radix-nova" name="select-invalid" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="select-rtl" direction="rtl" />

## API Reference

See the [Radix UI Select](https://www.radix-ui.com/docs/primitives/components/select#api-reference) documentation.
