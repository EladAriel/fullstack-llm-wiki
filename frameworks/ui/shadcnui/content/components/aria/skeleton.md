---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/aria/skeleton.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

---
title: Skeleton
description: Use to show a placeholder while content is loading.
base: aria
component: true
---

<ComponentPreview styleName="aria-nova" name="skeleton-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add skeleton
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="skeleton"
  title="components/ui/skeleton.tsx"
  styleName="aria-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Skeleton } from "@/components/ui/skeleton"
```

```tsx
<Skeleton className="h-[20px] w-[100px] rounded-full" />
```

## Avatar

<ComponentPreview styleName="aria-nova" name="skeleton-avatar" />

## Card

<ComponentPreview
  styleName="aria-nova"
  name="skeleton-card"
  previewClassName="h-80"
/>

## Text

<ComponentPreview styleName="aria-nova" name="skeleton-text" />

## Form

<ComponentPreview styleName="aria-nova" name="skeleton-form" />

## Table

<ComponentPreview styleName="aria-nova" name="skeleton-table" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="aria-nova" name="skeleton-rtl" direction="rtl" />
