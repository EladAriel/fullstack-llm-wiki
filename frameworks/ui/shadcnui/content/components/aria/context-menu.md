---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/aria/context-menu.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

---
title: Context Menu
description: Displays a menu of actions triggered by a right click.
base: aria
component: true
links:
  doc: https://react-aria.adobe.com/Menu
  api: https://react-aria.adobe.com/Menu#api
---

<ComponentPreview
  styleName="aria-nova"
  name="context-menu-demo"
  description="A context menu with sub menu items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add context-menu
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
  name="context-menu"
  title="components/ui/context-menu.tsx"
  styleName="aria-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Pressable } from "react-aria-components"

import {
  ContextMenu,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
```

```tsx showLineNumbers
<ContextMenuTrigger>
  <Pressable>
    <div role="button">Right click here</div>
  </Pressable>
  <ContextMenu>
    <ContextMenuItem>Profile</ContextMenuItem>
    <ContextMenuItem>Billing</ContextMenuItem>
    <ContextMenuItem>Team</ContextMenuItem>
    <ContextMenuItem>Subscription</ContextMenuItem>
  </ContextMenu>
</ContextMenuTrigger>
```

## Composition

Use the following composition to build a `ContextMenu`:

```text
ContextMenuTrigger
├── Pressable
└── ContextMenuContent
    ├── ContextMenuGroup
    │   ├── ContextMenuLabel
    │   ├── ContextMenuItem
    │   └── ContextMenuItem
    ├── ContextMenuSeparator
    ├── ContextMenuGroup
    │   ├── ContextMenuLabel
    │   ├── ContextMenuItem
    │   └── ContextMenuItem
    └── ContextMenuSub
        ├── ContextMenuSubTrigger
        └── ContextMenuSubContent
            └── ContextMenuGroup
                ├── ContextMenuItem
                └── ContextMenuItem
```

## Basic

A simple context menu with a few actions.

<ComponentPreview styleName="aria-nova" name="context-menu-basic" />

## Submenu

Use `ContextMenuSub` to nest secondary actions.

<ComponentPreview styleName="aria-nova" name="context-menu-submenu" />

## Shortcuts

Add `ContextMenuShortcut` to show keyboard hints.

<ComponentPreview styleName="aria-nova" name="context-menu-shortcuts" />

## Groups

Group related actions and separate them with dividers.

<ComponentPreview styleName="aria-nova" name="context-menu-groups" />

## Icons

Combine icons with labels for quick scanning.

<ComponentPreview styleName="aria-nova" name="context-menu-icons" />

## Checkboxes

Use `selectionMode="multiple"` for toggles.

<ComponentPreview styleName="aria-nova" name="context-menu-checkboxes" />

## Radio

Use `selectionMode="single"` for exclusive choices.

<ComponentPreview styleName="aria-nova" name="context-menu-radio" />

## Destructive

Use `variant="destructive"` to style the menu item as destructive.

<ComponentPreview styleName="aria-nova" name="context-menu-destructive" />

## Placement

Control submenu placement with the `placement` prop.

<ComponentPreview styleName="aria-nova" name="context-menu-sides" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="aria-nova"
  name="context-menu-rtl"
  direction="rtl"
/>

Use `placement="end"` to place the menu on the logical end side of the trigger.

```tsx showLineNumbers
<ContextMenuTrigger>
  <Pressable>
    <div role="button">Right click here</div>
  </Pressable>
  <ContextMenu placement="end">
    <ContextMenuItem>Profile</ContextMenuItem>
    <ContextMenuItem>Billing</ContextMenuItem>
    <ContextMenuItem>Team</ContextMenuItem>
    <ContextMenuItem>Subscription</ContextMenuItem>
  </ContextMenu>
</ContextMenuTrigger>
```

## API Reference

See the [React Aria](https://react-aria.adobe.com/Menu#api) documentation for more information.
