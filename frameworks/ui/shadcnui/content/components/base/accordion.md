---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/accordion.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Accordion
description: A vertically stacked set of interactive headings that each reveal a section of content.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/accordion
  api: https://base-ui.com/react/components/accordion#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="accordion-demo"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>

<TabsContent value="cli">

```bash
npx shadcn@latest add accordion
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
  name="accordion"
  title="components/ui/accordion.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"
```

```tsx showLineNumbers
<Accordion defaultValue={["item-1"]}>
  <AccordionItem value="item-1">
    <AccordionTrigger>Is it accessible?</AccordionTrigger>
    <AccordionContent>
      Yes. It adheres to the WAI-ARIA design pattern.
    </AccordionContent>
  </AccordionItem>
</Accordion>
```

## Composition

Use the following composition to build an `Accordion`:

```text
Accordion
├── AccordionItem
│   ├── AccordionTrigger
│   └── AccordionContent
└── AccordionItem
    ├── AccordionTrigger
    └── AccordionContent
```

## Examples

### Basic

A basic accordion that shows one item at a time. The first item is open by default.

<ComponentPreview
  styleName="base-nova"
  name="accordion-basic"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

### Multiple

Use the `multiple` prop to allow multiple items to be open at the same time.

<ComponentPreview
  styleName="base-nova"
  name="accordion-multiple"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[450px]"
/>

### Disabled

Use the `disabled` prop on `AccordionItem` to disable individual items.

<ComponentPreview
  styleName="base-nova"
  name="accordion-disabled"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

### Borders

Add `border` to the `Accordion` and `border-b last:border-b-0` to the `AccordionItem` to add borders to the items.

<ComponentPreview
  styleName="base-nova"
  name="accordion-borders"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[300px]"
/>

### Card

Wrap the `Accordion` in a `Card` component.

<ComponentPreview
  styleName="base-nova"
  name="accordion-card"
  align="start"
  previewClassName="*:data-[slot=accordion]:max-w-sm h-[435px]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="accordion-rtl"
  align="start"
  direction="rtl"
/>

## API Reference

See the [Base UI](https://base-ui.com/react/components/accordion#api-reference) documentation for more information.
