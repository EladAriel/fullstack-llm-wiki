---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/aria/label.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

---
title: Label
description: Renders an accessible label associated with controls.
base: aria
component: true
links:
  doc: https://react-aria.adobe.com/TextField
  api: https://react-aria.adobe.com/TextField#api
---

<ComponentPreview styleName="aria-nova" name="label-demo" />

<Callout>
  For form fields, use the [Field](/docs/components/aria/field) component which
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
npm install react-aria-components
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="label"
  title="components/ui/label.tsx"
  styleName="aria-nova"
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

For form fields, use the [Field](/docs/components/aria/field) component which
includes built-in `FieldLabel`, `FieldDescription`, and `FieldError` components.

```tsx
<Field>
  <FieldLabel htmlFor="email">Your email address</FieldLabel>
  <Input id="email" />
</Field>
```

<ComponentPreview
  styleName="aria-nova"
  name="field-demo"
  previewClassName="h-[44rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="aria-nova" name="label-rtl" direction="rtl" />
