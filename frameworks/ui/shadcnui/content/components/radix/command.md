---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/command.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Command
description: Command menu for search and quick actions.
base: radix
component: true
links:
  doc: https://github.com/dip/cmdk
---

<ComponentPreview
  styleName="radix-nova"
  name="command-demo"
  align="start"
  previewClassName="h-[24.5rem]"
/>

## About

The `<Command />` component uses the [`cmdk`](https://github.com/dip/cmdk) component by [Dip](https://www.dip.org/).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add command
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install cmdk
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="command"
  title="components/ui/command.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from "@/components/ui/command"
```

```tsx showLineNumbers
<Command className="max-w-sm rounded-lg border">
  <CommandInput placeholder="Type a command or search..." />
  <CommandList>
    <CommandEmpty>No results found.</CommandEmpty>
    <CommandGroup heading="Suggestions">
      <CommandItem>Calendar</CommandItem>
      <CommandItem>Search Emoji</CommandItem>
      <CommandItem>Calculator</CommandItem>
    </CommandGroup>
    <CommandSeparator />
    <CommandGroup heading="Settings">
      <CommandItem>Profile</CommandItem>
      <CommandItem>Billing</CommandItem>
      <CommandItem>Settings</CommandItem>
    </CommandGroup>
  </CommandList>
</Command>
```

## Composition

Use the following composition to build a `Command`:

```text
Command
├── CommandInput
└── CommandList
    ├── CommandEmpty
    ├── CommandGroup
    │   ├── CommandItem
    │   └── CommandItem
    ├── CommandSeparator
    └── CommandGroup
        ├── CommandItem
        └── CommandItem
```

## Examples

### Basic

A simple command menu in a dialog.

<ComponentPreview styleName="radix-nova" name="command-basic" />

### Shortcuts

<ComponentPreview styleName="radix-nova" name="command-shortcuts" />

### Groups

A command menu with groups, icons and separators.

<ComponentPreview styleName="radix-nova" name="command-groups" />

### Scrollable

Scrollable command menu with multiple items.

<ComponentPreview styleName="radix-nova" name="command-scrollable" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="command-rtl"
  direction="rtl"
  align="start"
  previewClassName="h-[24.5rem]"
/>

## API Reference

See the [cmdk](https://github.com/dip/cmdk) documentation for more information.
