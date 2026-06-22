---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/radix/hover-card.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Hover Card
description: For sighted users to preview content available behind a link.
base: radix
component: true
links:
  doc: https://www.radix-ui.com/docs/primitives/components/hover-card
  api: https://www.radix-ui.com/docs/primitives/components/hover-card#api-reference
---

<ComponentPreview
  styleName="radix-nova"
  name="hover-card-demo"
  previewClassName="h-80"
/>

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add hover-card
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
  name="hover-card"
  title="components/ui/hover-card.tsx"
  styleName="radix-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx showLineNumbers
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card"
```

```tsx showLineNumbers
<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent>
    The React Framework – created and maintained by @vercel.
  </HoverCardContent>
</HoverCard>
```

## Composition

Use the following composition to build a `HoverCard`:

```text
HoverCard
├── HoverCardTrigger
└── HoverCardContent
```

## Trigger Delays

Use `openDelay` and `closeDelay` on the `HoverCard` to control when the card opens and
closes.

```tsx showLineNumbers
<HoverCard openDelay={100} closeDelay={200}>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent>Content</HoverCardContent>
</HoverCard>
```

## Positioning

Use the `side` and `align` props on `HoverCardContent` to control placement.

```tsx showLineNumbers
<HoverCard>
  <HoverCardTrigger>Hover</HoverCardTrigger>
  <HoverCardContent side="top" align="start">
    Content
  </HoverCardContent>
</HoverCard>
```

## Examples

### Basic

<ComponentPreview
  styleName="radix-nova"
  name="hover-card-demo"
  previewClassName="h-80"
/>

### Sides

<ComponentPreview
  styleName="radix-nova"
  name="hover-card-sides"
  previewClassName="h-[22rem]"
/>

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview
  styleName="radix-nova"
  name="hover-card-rtl"
  direction="rtl"
  previewClassName="h-80"
/>

## API Reference

See the [Radix UI](https://www.radix-ui.com/docs/primitives/components/hover-card#api-reference) documentation for more information.
