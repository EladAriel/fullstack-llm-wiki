---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/dropdown-menu.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.985821Z"
---
# Dropdown Menu

---
title: Dropdown Menu
description: Displays a menu to the user — such as a set of actions or functions — triggered by a button.
featured: true
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/dropdown-menu
  api: https://www.radix-ui.com/docs/primitives/components/dropdown-menu#api-reference
---

<ComponentPreview
  styleName="radix-nova"
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
npm install radix-ui
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="dropdown-menu"
  title="components/ui/dropdown-menu.tsx"
  styleName="radix-nova"
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
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
```

```tsx showLineNumbers
<DropdownMenu>
  <DropdownMenuTrigger asChild>
    <Button variant="outline">Open</Button>
  </DropdownMenuTrigger>
  <DropdownMenuContent>
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
  </DropdownMenuContent>
</DropdownMenu>
```

## Composition

Use the following composition to build a `DropdownMenu`:

```text
DropdownMenu
├── DropdownMenuTrigger
└── DropdownMenuContent
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   ├── DropdownMenuItem
    │   └── DropdownMenuItem
    ├── DropdownMenuSeparator
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   ├── DropdownMenuCheckboxItem
    │   └── DropdownMenuCheckboxItem
    ├── DropdownMenuSeparator
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   └── DropdownMenuRadioGroup
    │       ├── DropdownMenuRadioItem
    │       └── DropdownMenuRadioItem
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

<ComponentPreview styleName="radix-nova" name="dropdown-menu-basic" />

## Submenu

Use `DropdownMenuSub` to nest secondary actions.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-submenu" />

## Shortcuts

Add `DropdownMenuShortcut` to show keyboard hints.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-shortcuts" />

## Icons

Combine icons with labels for quick scanning.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-icons" />

## Checkboxes

Use `DropdownMenuCheckboxItem` for toggles.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-checkboxes" />

## Checkboxes Icons

Add icons to checkbox items.

<ComponentPreview
  styleName="radix-nova"
  name="dropdown-menu-checkboxes-icons"
/>

## Radio Group

Use `DropdownMenuRadioGroup` for exclusive choices.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-radio-group" />

## Radio Icons

Show radio options with icons.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-radio-icons" />

## Destructive

Use `variant="destructive"` for irreversible actions.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-destructive" />

## Avatar

An account switcher dropdown triggered by an avatar.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-avatar" />

## Complex

A richer example combining groups, icons, and submenus.

<ComponentPreview styleName="radix-nova" name="dropdown-menu-complex" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="dropdown-menu-rtl"
  direction="rtl"
/>

## API Reference

See the [Radix UI documentation](https://www.radix-ui.com/docs/primitives/components/dropdown-menu) for the full API reference.
