---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/sonner.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Sonner
description: An opinionated toast component for React.
base: base
component: true
links:
  doc: https://sonner.emilkowal.ski
---

<ComponentPreview styleName="base-nova" name="sonner-demo" />

## About

Sonner is built and maintained by [emilkowalski](https://twitter.com/emilkowalski).

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

<Steps className="mb-0 pt-2">

<Step>Run the following command:</Step>

```bash
npx shadcn@latest add sonner
```

<Step>Add the Toaster component.</Step>

```tsx title="app/layout.tsx" {1,9} showLineNumbers
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <main>{children}</main>
        <Toaster />
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Install the following dependencies:</Step>

```bash
npm install sonner next-themes
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="sonner"
  title="components/ui/sonner.tsx"
  styleName="base-nova"
/>

<Step>Add the Toaster component.</Step>

```tsx showLineNumbers title="app/layout.tsx" {1,8}
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body>
        <Toaster />
        <main>{children}</main>
      </body>
    </html>
  )
}
```

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { toast } from "sonner"
```

```tsx
toast("Event has been created.")
```

## Examples

### Types

<ComponentPreview styleName="base-nova" name="sonner-types" />

### Description

<ComponentPreview styleName="base-nova" name="sonner-description" />

### Position

Use the `position` prop to change the position of the toast.

<ComponentPreview styleName="base-nova" name="sonner-position" />

## API Reference

See the [Sonner API Reference](https://sonner.emilkowal.ski/getting-started) for more information.
