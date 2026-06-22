---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/label.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Label
description: Renders an accessible label associated with controls.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/label
  api: https://base-ui.com/react/components/label#api-reference
---

<ComponentPreview styleName="base-nova" name="label-demo" />

<Callout>
  For form fields, use the [Field](/docs/components/base/field) component which
  includes built-in label, description, and error handling.
</Callout>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add label
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
  name="label"
  title="components/ui/label.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Label } from "@/components/ui/label"
```

```tsx
<Label htmlFor="email">Your email address</Label>
```

## Label in Field

For form fields, use the [Field](/docs/components/base/field) component which
includes built-in `FieldLabel`, `FieldDescription`, and `FieldError` components.

```tsx
<Field>
  <FieldLabel htmlFor="email">Your email address</FieldLabel>
  <Input id="email" />
</Field>
```

<ComponentPreview
  styleName="base-nova"
  name="field-demo"
  previewClassName="h-[44rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="label-rtl" direction="rtl" />

## API Reference

See the [Base UI Label](https://base-ui.com/react/components/label#api-reference) documentation for more information.
