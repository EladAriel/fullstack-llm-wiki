---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/aria/tabs.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

---
title: Tabs
description: A set of layered sections of content—known as tab panels—that are displayed one at a time.
base: aria
component: true
links:
  doc: https://react-aria.adobe.com/Tabs
  api: https://react-aria.adobe.com/Tabs#api
---

<ComponentPreview
  styleName="aria-nova"
  name="tabs-demo"
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
npx shadcn@latest add tabs
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
  name="tabs"
  title="components/ui/tabs.tsx"
  styleName="aria-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
```

```tsx showLineNumbers
<Tabs defaultSelectedKey="account" className="w-[400px]">
  <TabsList>
    <TabsTrigger id="account">Account</TabsTrigger>
    <TabsTrigger id="password">Password</TabsTrigger>
  </TabsList>
  <TabsContent id="account">Make changes to your account here.</TabsContent>
  <TabsContent id="password">Change your password here.</TabsContent>
</Tabs>
```

## Composition

Use the following composition to build `Tabs`:

```text
Tabs
├── TabsList
│   ├── TabsTrigger
│   └── TabsTrigger
├── TabsContent
└── TabsContent
```

## Line

Use the `variant="line"` prop on `TabsList` for a line style.

<ComponentPreview styleName="aria-nova" name="tabs-line" />

## Vertical

Use `orientation="vertical"` for vertical tabs.

<ComponentPreview styleName="aria-nova" name="tabs-vertical" />

## Disabled

<ComponentPreview styleName="aria-nova" name="tabs-disabled" />

## Icons

<ComponentPreview styleName="aria-nova" name="tabs-icons" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="aria-nova" name="tabs-rtl" direction="rtl" />

## API Reference

See the [React Aria Tabs](https://react-aria.adobe.com/Tabs#api) documentation.
