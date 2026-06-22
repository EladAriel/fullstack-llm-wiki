---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/skeleton.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Skeleton
description: Use to show a placeholder while content is loading.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="skeleton-demo" />

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
  styleName="base-nova"
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

## Examples

### Avatar

<ComponentPreview styleName="base-nova" name="skeleton-avatar" />

### Card

<ComponentPreview
  styleName="base-nova"
  name="skeleton-card"
  previewClassName="h-80"
/>

### Text

<ComponentPreview styleName="base-nova" name="skeleton-text" />

### Form

<ComponentPreview styleName="base-nova" name="skeleton-form" />

### Table

<ComponentPreview styleName="base-nova" name="skeleton-table" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="skeleton-rtl" direction="rtl" />
