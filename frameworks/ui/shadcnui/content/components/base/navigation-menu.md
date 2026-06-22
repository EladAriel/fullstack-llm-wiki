---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/navigation-menu.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Navigation Menu
description: A collection of links for navigating websites.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/navigation-menu
  api: https://base-ui.com/react/components/navigation-menu#api-reference
---

<ComponentPreview
  styleName="base-nova"
  name="navigation-menu-demo"
  previewClassName="h-96"
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
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="navigation-menu"
  title="components/ui/navigation-menu.tsx"
  styleName="base-nova"
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

Use the `render` prop to compose a custom link component such as Next.js `Link`.

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
      <NavigationMenuLink
        render={<Link href="/docs" />}
        className={navigationMenuTriggerStyle()}
      >
        Documentation
      </NavigationMenuLink>
    </NavigationMenuItem>
  )
}
```

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="base-nova"
  name="navigation-menu-rtl"
  direction="rtl"
  previewClassName="h-96"
/>

## API Reference

See the [Base UI Navigation Menu](https://base-ui.com/react/components/navigation-menu#api-reference) documentation for more information.
