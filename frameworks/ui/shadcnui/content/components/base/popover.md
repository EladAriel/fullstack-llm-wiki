---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/popover.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Popover
description: Displays rich content in a portal, triggered by a button.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/popover
  api: https://base-ui.com/react/components/popover#api-reference
---

<ComponentPreview styleName="base-nova" name="popover-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add popover
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
  name="popover"
  title="components/ui/popover.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Popover,
  PopoverContent,
  PopoverDescription,
  PopoverHeader,
  PopoverTitle,
  PopoverTrigger,
} from "@/components/ui/popover"
```

```tsx showLineNumbers
<Popover>
  <PopoverTrigger render={<Button variant="outline" />}>
    Open Popover
  </PopoverTrigger>
  <PopoverContent>
    <PopoverHeader>
      <PopoverTitle>Title</PopoverTitle>
      <PopoverDescription>Description text here.</PopoverDescription>
    </PopoverHeader>
  </PopoverContent>
</Popover>
```

## Composition

Use the following composition to build a `Popover`:

```text
Popover
├── PopoverTrigger
└── PopoverContent
```

## Examples

### Basic

A simple popover with a header, title, and description.

<ComponentPreview styleName="base-nova" name="popover-basic" />

### Align

Use the `align` prop on `PopoverContent` to control the horizontal alignment.

<ComponentPreview styleName="base-nova" name="popover-alignments" />

### With Form

A popover with form fields inside.

<ComponentPreview styleName="base-nova" name="popover-form" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="popover-rtl" direction="rtl" />

## API Reference

See the [Base UI Popover](https://base-ui.com/react/components/popover#api-reference) documentation.
