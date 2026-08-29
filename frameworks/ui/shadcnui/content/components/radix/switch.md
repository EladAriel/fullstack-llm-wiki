---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/switch.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.977578Z"
---
# Switch

---
title: Switch
description: A control that allows the user to toggle between checked and not checked.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/switch
  api: https://www.radix-ui.com/docs/primitives/components/switch#api-reference
---

<ComponentPreview styleName="radix-nova" name="switch-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add switch
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
  name="switch"
  title="components/ui/switch.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Switch } from "@/components/ui/switch"
```

```tsx
<Switch />
```

## Description

<ComponentPreview styleName="radix-nova" name="switch-description" />

## Choice Card

Card-style selection where `FieldLabel` wraps the entire `Field` for a clickable card pattern.

<ComponentPreview styleName="radix-nova" name="switch-choice-card" />

## Disabled

Add the `disabled` prop to the `Switch` component to disable the switch. Add the `data-disabled` prop to the `Field` component for styling.

<ComponentPreview styleName="radix-nova" name="switch-disabled" />

## Invalid

Add the `aria-invalid` prop to the `Switch` component to indicate an invalid state. Add the `data-invalid` prop to the `Field` component for styling.

<ComponentPreview styleName="radix-nova" name="switch-invalid" />

## Size

Use the `size` prop to change the size of the switch.

<ComponentPreview styleName="radix-nova" name="switch-sizes" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="switch-rtl" direction="rtl" />

## API Reference

See the [Radix Switch](https://www.radix-ui.com/docs/primitives/components/switch#api-reference) documentation.
