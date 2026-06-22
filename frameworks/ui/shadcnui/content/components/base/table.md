---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/table.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Table
description: A responsive table component.
base: base
component: true
---

<ComponentPreview
  styleName="base-nova"
  name="table-demo"
  previewClassName="h-[30rem]"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add table
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="table"
  title="components/ui/table.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
```

```tsx showLineNumbers
<Table>
  <TableCaption>A list of your recent invoices.</TableCaption>
  <TableHeader>
    <TableRow>
      <TableHead className="w-[100px]">Invoice</TableHead>
      <TableHead>Status</TableHead>
      <TableHead>Method</TableHead>
      <TableHead className="text-right">Amount</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    <TableRow>
      <TableCell className="font-medium">INV001</TableCell>
      <TableCell>Paid</TableCell>
      <TableCell>Credit Card</TableCell>
      <TableCell className="text-right">$250.00</TableCell>
    </TableRow>
  </TableBody>
</Table>
```

## Composition

Use the following composition to build a `Table`:

```text
Table
├── TableCaption
├── TableHeader
│   └── TableRow
│       ├── TableHead
│       ├── TableHead
│       ├── TableHead
│       └── TableHead
├── TableBody
│   ├── TableRow
│   │   ├── TableCell
│   │   ├── TableCell
│   │   ├── TableCell
│   │   └── TableCell
│   └── TableRow
│       ├── TableCell
│       ├── TableCell
│       ├── TableCell
│       └── TableCell
└── TableFooter
```

## Examples

### Footer

Use the `<TableFooter />` component to add a footer to the table.

<ComponentPreview styleName="base-nova" name="table-footer" />

### Actions

A table showing actions for each row using a `<DropdownMenu />` component.

<ComponentPreview styleName="base-nova" name="table-actions" />

## Data Table

You can use the `<Table />` component to build more complex data tables. Combine it with [@tanstack/react-table](https://tanstack.com/table/v8) to create tables with sorting, filtering and pagination.

See the [Data Table](/docs/components/data-table) documentation for more information.

You can also see an example of a data table in the [Tasks](/examples/tasks) demo.

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="table-rtl"
  direction="rtl"
  previewClassName="h-auto"
/>
