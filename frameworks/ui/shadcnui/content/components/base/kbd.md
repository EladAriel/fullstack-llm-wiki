---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/components/base/kbd.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Kbd
description: Used to display textual user input from keyboard.
base: base
component: true
---

<ComponentPreview styleName="base-nova" name="kbd-demo" />

## Installation

<CodeTabs>

<TabsList>
  <TabsTrigger value="cli">Command</TabsTrigger>
  <TabsTrigger value="manual">Manual</TabsTrigger>
</TabsList>
<TabsContent value="cli">

```bash
npx shadcn@latest add kbd
```

</TabsContent>

<TabsContent value="manual">

<Steps className="mb-0 pt-2">

<Step>Copy and paste the following code into your project.</Step>

<ComponentSource
  name="kbd"
  title="components/ui/kbd.tsx"
  styleName="base-nova"
/>

<Step>Update the import paths to match your project setup.</Step>

</Steps>

</TabsContent>

</CodeTabs>

## Usage

```tsx
import { Kbd } from "@/components/ui/kbd"
```

```tsx
<Kbd>Ctrl</Kbd>
```

## Composition

Use the following composition to build `Kbd` and `KbdGroup`:

```text
Kbd
KbdGroup
├── Kbd
└── Kbd
```

## Examples

### Group

Use the `KbdGroup` component to group keyboard keys together.

<ComponentPreview styleName="base-nova" name="kbd-group" />

### Button

Use the `Kbd` component inside a `Button` component to display a keyboard key inside a button.

<ComponentPreview styleName="base-nova" name="kbd-button" />

### Tooltip

You can use the `Kbd` component inside a `Tooltip` component to display a tooltip with a keyboard key.

<ComponentPreview styleName="base-nova" name="kbd-tooltip" />

### Input Group

You can use the `Kbd` component inside a `InputGroupAddon` component to display a keyboard key inside an input group.

<ComponentPreview styleName="base-nova" name="kbd-input-group" />

## RTL

To enable RTL support in shadcn/ui, see the [RTL configuration guide](/docs/rtl).

<ComponentPreview styleName="base-nova" name="kbd-rtl" direction="rtl" />

## API Reference

### Kbd

Use the `Kbd` component to display a keyboard key.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | ``      |

```tsx
<Kbd>Ctrl</Kbd>
```

### KbdGroup

Use the `KbdGroup` component to group `Kbd` components together.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | ``      |

```tsx
<KbdGroup>
  <Kbd>Ctrl</Kbd>
  <Kbd>B</Kbd>
</KbdGroup>
```
