---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/aria/dropdown-menu.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.973928Z"
---
# Dropdown Menu

---
title: Dropdown Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
featured: true
base: aria
component: true
links:
  doc: https://react-aria.adobe.com/Menu
  api: https://react-aria.adobe.com/Menu#api
---

<ComponentPreview
  styleName="aria-nova"
  name="dropdown-menu-demo"
  description="A dropdown menu with icons, shortcuts and sub menu items."
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add dropdown-menu
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
  name="dropdown-menu"
  title="components/ui/dropdown-menu.tsx"
  styleName="aria-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
```

```tsx showLineNumbers
<DropdownMenuTrigger>
  <Button variant="outline">Open</Button>
  <DropdownMenu>
    <DropdownMenuGroup>
      <DropdownMenuLabel>My Account</DropdownMenuLabel>
      <DropdownMenuItem>Profile</DropdownMenuItem>
      <DropdownMenuItem>Billing</DropdownMenuItem>
    </DropdownMenuGroup>
    <DropdownMenuSeparator />
    <DropdownMenuGroup>
      <DropdownMenuItem>Team</DropdownMenuItem>
      <DropdownMenuItem>Subscription</DropdownMenuItem>
    </DropdownMenuGroup>
  </DropdownMenu>
</DropdownMenuTrigger>
```

## Composition

Use the following composition to build a `DropdownMenu`:

```text
DropdownMenuTrigger
├── Button
└── DropdownMenu
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   ├── DropdownMenuItem
    │   └── DropdownMenuItem
    ├── DropdownMenuSeparator
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   ├── DropdownMenuItem
    │   └── DropdownMenuItem
    └── DropdownMenuSub
        ├── DropdownMenuSubTrigger
        └── DropdownMenuSubContent
            └── DropdownMenuGroup
                ├── DropdownMenuLabel
                ├── DropdownMenuItem
                └── DropdownMenuItem
```

## Basic

A basic dropdown menu with labels and separators.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-basic" />

## Submenu

Use `DropdownMenuSub` to nest secondary actions.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-submenu" />

## Shortcuts

Add `DropdownMenuShortcut` to show keyboard hints.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-shortcuts" />

## Icons

Combine icons with labels for quick scanning.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-icons" />

## Checkboxes

Use `selectionMode="multiple"` for toggles.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-checkboxes" />

## Checkboxes Icons

Add icons to checkbox items.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-checkboxes-icons" />

## Radio Group

Use `selectionMode="single"` for exclusive choices.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-radio-group" />

## Radio Icons

Show radio options with icons.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-radio-icons" />

## Destructive

Use `variant="destructive"` for irreversible actions.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-destructive" />

## Avatar

An account switcher dropdown triggered by an avatar.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-avatar" />

## Complex

A richer example combining groups, icons, and submenus.

<ComponentPreview styleName="aria-nova" name="dropdown-menu-complex" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="aria-nova"
  name="dropdown-menu-rtl"
  direction="rtl"
/>

## API Reference

See the [React Aria documentation](https://react-aria.adobe.com/Menu) for the full API reference.
