---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/toast.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

---
title: Toast
description: A succinct message that is displayed temporarily.
base: base
component: true
links:
  doc: https://base-ui.com/react/components/toast
  api: https://base-ui.com/react/components/toast#api-reference
---

<ComponentPreview styleName="base-nova" name="toast-demo" />

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
npx shadcn@latest add toast
```

<Step>Add the Toaster component.</Step>

```tsx title="app/layout.tsx" {1,9} showLineNumbers
import { Toaster } from "@/components/ui/toast"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
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

<Step>Install the following dependency:</Step>

```bash
npm install @base-ui/react
```

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="toast"
  title="components/ui/toast.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

<Step>Add the Toaster component.</Step>

```tsx title="app/layout.tsx" {1,8} showLineNumbers
import { Toaster } from "@/components/ui/toast"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
        <Toaster />
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
import { toast } from "@/components/ui/toast"
```

```tsx
toast.add({
  title: "Event created",
  description: "Sunday, December 3 at 9:00 AM",
})
```

## Types

Set the `type` option to render a status icon. The built-in renderer recognizes
`success`, `info`, `warning`, `error`, and `loading`.

<ComponentPreview styleName="base-nova" name="toast-types" />

## Action

Pass button props with `actionProps` to render an action.

```tsx
const id = toast.add({
  title: "Event created",
  actionProps: {
    children: "Undo",
    onClick() {
      toast.close(id)
    },
  },
})
```

## Promise

Use `toast.promise` to update one toast as an asynchronous task moves through
loading, success, and error states.

<ComponentPreview styleName="base-nova" name="toast-promise" />

## API Reference

See the [Base UI Toast documentation](https://base-ui.com/react/components/toast)
for details about manager options, stacking, swipe dismissal, and the primitive
API.
