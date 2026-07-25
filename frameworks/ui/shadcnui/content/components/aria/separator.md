---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/aria/separator.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

---
title: Separator
description: Visually or semantically separates content.
base: aria
component: true
links:
  doc: https://react-aria.adobe.com/Separator
  api: https://react-aria.adobe.com/Separator#api
---

<ComponentPreview styleName="aria-nova" name="separator-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add separator
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
  name="separator"
  title="components/ui/separator.tsx"
  styleName="aria-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Separator } from "@/components/ui/separator"
```

```tsx showLineNumbers
<Separator />
```

## Vertical

Use `orientation="vertical"` for a vertical separator.

<ComponentPreview styleName="aria-nova" name="separator-vertical" />

## Menu

Vertical separators between menu items with descriptions.

<ComponentPreview styleName="aria-nova" name="separator-menu" />

## List

Horizontal separators between list items.

<ComponentPreview styleName="aria-nova" name="separator-list" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="aria-nova" name="separator-rtl" direction="rtl" />

## API Reference

See the [React Aria Separator](https://react-aria.adobe.com/Separator#api) documentation.
