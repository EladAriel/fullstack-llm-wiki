---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/badge.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Badge
description: Displays a badge or a component that looks like a badge.
base: radix
component: true
---

<ComponentPreview styleName="radix-nova" name="badge-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add badge
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource name="badge" title="components/ui/badge.tsx" />

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Badge } from "@/components/ui/badge"
```

```tsx
<Badge variant="default | outline | secondary | destructive">Badge</Badge>
```

## Examples

### Variants

Use the `variant` prop to change the variant of the badge.

<ComponentPreview styleName="radix-nova" name="badge-variants" />

### With Icon

You can render an icon inside the badge. Use `data-icon="inline-start"` to render the icon on the left and `data-icon="inline-end"` to render the icon on the right.

<ComponentPreview styleName="radix-nova" name="badge-icon" />

### With Spinner

You can render a spinner inside the badge. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` prop to the spinner.

<ComponentPreview styleName="radix-nova" name="badge-spinner" />

### Link

Use the `asChild` prop to render a link as a badge.

<ComponentPreview styleName="radix-nova" name="badge-link" />

### Custom Colors

You can customize the colors of a badge by adding custom classes such as `bg-green-50 dark:bg-green-800` to the `Badge` component.

<ComponentPreview styleName="radix-nova" name="badge-colors" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="radix-nova" name="badge-rtl" direction="rtl" />

## API Reference

### Badge

The `Badge` component displays a badge or a component that looks like a badge.

| Prop        | Type                                                                          | Default     |
| ----------- | ----------------------------------------------------------------------------- | ----------- |
| `variant`   | `"default" \| "secondary" \| "destructive" \| "outline" \| "ghost" \| "link"` | `"default"` |
| `className` | `string`                                                                      | -           |
