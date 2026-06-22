---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/separator.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Separator
description: Visually or semantically separates content.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/separator
  api: https://www.radix-ui.com/docs/primitives/components/separator#api-reference
---

<ComponentPreview styleName="radix-nova" name="separator-demo" />

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
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="separator"
  title="components/ui/separator.tsx"
  styleName="radix-nova"
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

## Examples

### Vertical

Use `orientation="vertical"` for a vertical separator.

<ComponentPreview styleName="radix-nova" name="separator-vertical" />

### Menu

Vertical separators between menu items with descriptions.

<ComponentPreview styleName="radix-nova" name="separator-menu" />

### List

Horizontal separators between list items.

<ComponentPreview styleName="radix-nova" name="separator-list" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="separator-rtl" direction="rtl" />

## API Reference

See the [Radix UI Separator](https://www.radix-ui.com/docs/primitives/components/separator#api-reference) documentation.
