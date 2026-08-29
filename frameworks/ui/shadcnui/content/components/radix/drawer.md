---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/drawer.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.980237Z"
---
# Drawer

---
title: Drawer
description: A drawer component for React.
base: radix
component: true
links:
  doc: https://vaul.emilkowal.ski/getting-started
---

<ComponentPreview styleName="radix-nova" name="drawer-demo" />

## About

Drawer is built on top of [Vaul](https://github.com/emilkowalski/vaul) by [emilkowalski](https://twitter.com/emilkowalski).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add drawer
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install vaul
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="drawer"
  title="components/ui/drawer.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"
```

```tsx showLineNumbers
<Drawer>
  <DrawerTrigger>Open</DrawerTrigger>
  <DrawerContent>
    <DrawerHeader>
      <DrawerTitle>Are you absolutely sure?</DrawerTitle>
      <DrawerDescription>This action cannot be undone.</DrawerDescription>
    </DrawerHeader>
    <DrawerFooter>
      <Button>Submit</Button>
      <DrawerClose>
        <Button variant="outline">Cancel</Button>
      </DrawerClose>
    </DrawerFooter>
  </DrawerContent>
</Drawer>
```

## Composition

Use the following composition to build a `Drawer`:

```text
Drawer
├── DrawerTrigger
└── DrawerContent
    ├── DrawerHeader
    │   ├── DrawerTitle
    │   └── DrawerDescription
    └── DrawerFooter
```

## Scrollable Content

Keep actions visible while the content scrolls.

<ComponentPreview styleName="radix-nova" name="drawer-scrollable-content" />

## Sides

Use the `direction` prop to set the side of the drawer. Available options are `top`, `right`, `bottom`, and `left`.

<ComponentPreview styleName="radix-nova" name="drawer-sides" />

## Responsive Dialog

You can combine the `Dialog` and `Drawer` components to create a responsive dialog. This renders a `Dialog` component on desktop and a `Drawer` on mobile.

<ComponentPreview styleName="radix-nova" name="drawer-dialog" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="drawer-rtl" direction="rtl" />

## API Reference

See the [Vaul documentation](https://vaul.emilkowal.ski/getting-started) for the full API reference.
