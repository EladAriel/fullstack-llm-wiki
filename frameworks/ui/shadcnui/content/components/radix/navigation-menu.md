---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/navigation-menu.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Navigation Menu
description: A collection of links for navigating websites.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/navigation-menu
  api: https://www.radix-ui.com/docs/primitives/components/navigation-menu#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="navigation-menu-demo"
  previewClassName="h-96"
  className="overflow-visible"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add navigation-menu
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
  name="navigation-menu"
  title="components/ui/navigation-menu.tsx"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu"
```

```tsx showLineNumbers
<NavigationMenu>
  <NavigationMenuList>
    <NavigationMenuItem>
      <NavigationMenuTrigger>Item One</NavigationMenuTrigger>
      <NavigationMenuContent>
        <NavigationMenuLink>Link</NavigationMenuLink>
      </NavigationMenuContent>
    </NavigationMenuItem>
  </NavigationMenuList>
</NavigationMenu>
```

## Composition

Use the following composition to build a `NavigationMenu`:

```text
NavigationMenu
├── NavigationMenuList
│   ├── NavigationMenuItem
│   │   ├── NavigationMenuTrigger
│   │   └── NavigationMenuContent
│   │       ├── NavigationMenuLink
│   │       └── NavigationMenuLink
│   └── NavigationMenuItem
│       └── NavigationMenuLink
└── NavigationMenuIndicator
```

## Link Component

Use the `asChild` prop to compose a custom link component such as Next.js `Link`.

```tsx showLineNumbers
import Link from "next/link"

import {
  NavigationMenuItem,
  NavigationMenuLink,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"

export function NavigationMenuDemo() {
  return (
    <NavigationMenuItem>
      <NavigationMenuLink asChild className={navigationMenuTriggerStyle()}>
        <Link href="/docs">Documentation</Link>
      </NavigationMenuLink>
    </NavigationMenuItem>
  )
}
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="navigation-menu-rtl"
  direction="rtl"
  previewClassName="h-96"
  className="overflow-visible"
/>

## API Reference

See the [Radix UI Navigation Menu](https://www.radix-ui.com/docs/primitives/components/navigation-menu#api-reference) documentation for more information.
