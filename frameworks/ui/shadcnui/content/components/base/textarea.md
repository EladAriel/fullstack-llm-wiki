---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/textarea.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.997774Z"
---
# Textarea

---
title: Textarea
description: Displays a form textarea or a component that looks like a textarea.
base: base
component: true
---

<ComponentPreview
  styleName="base-nova"
  name="textarea-demo"
  previewClassName="*:max-w-xs"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add textarea
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="textarea"
  title="components/ui/textarea.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Textarea } from "@/components/ui/textarea"
```

```tsx
<Textarea />
```

## Field

Use `Field`, `FieldLabel`, and `FieldDescription` to create a textarea with a label and description.

<ComponentPreview
  styleName="base-nova"
  name="textarea-field"
  previewClassName="*:max-w-xs"
/>

## Disabled

Use the `disabled` prop to disable the textarea. To style the disabled state, add the `data-disabled` attribute to the `Field` component.

<ComponentPreview
  styleName="base-nova"
  name="textarea-disabled"
  previewClassName="*:max-w-xs"
/>

## Invalid

Use the `aria-invalid` prop to mark the textarea as invalid. To style the invalid state, add the `data-invalid` attribute to the `Field` component.

<ComponentPreview
  styleName="base-nova"
  name="textarea-invalid"
  previewClassName="*:max-w-xs"
/>

## Button

Pair with `Button` to create a textarea with a submit button.

<ComponentPreview
  styleName="base-nova"
  name="textarea-button"
  previewClassName="*:max-w-xs"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="textarea-rtl" direction="rtl" />
