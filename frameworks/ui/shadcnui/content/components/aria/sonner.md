---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/aria/sonner.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

---
title: Sonner
description: An opinionated toast component for React.
base: aria
component: true
links:
  doc: https://sonner.emilkowal.ski
---

<ComponentPreview styleName="aria-nova" name="sonner-demo" />

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

<Step>Add the Toaster component</Step>

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
  styleName="aria-nova"
/>

<Step>Add the Toaster component</Step>

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

## Types

<ComponentPreview styleName="aria-nova" name="sonner-types" />

## Description

<ComponentPreview styleName="aria-nova" name="sonner-description" />

## Position

Use the `position` prop to change the position of the toast.

<ComponentPreview styleName="aria-nova" name="sonner-position" />

## API Reference

See the [Sonner API Reference](https://sonner.emilkowal.ski/getting-started) for more information.
