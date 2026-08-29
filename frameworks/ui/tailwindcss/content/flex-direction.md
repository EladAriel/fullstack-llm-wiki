---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/flex-direction.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.752291Z"
---
# Flex Direction

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "flex-direction";
export const description = "Utilities for controlling the direction of flex items.";

<ApiTable
  rows={[
    ["flex-row", "flex-direction: row;"],
    ["flex-row-reverse", "flex-direction: row-reverse;"],
    ["flex-col", "flex-direction: column;"],
    ["flex-col-reverse", "flex-direction: column-reverse;"],
  ]}
/>

## Examples

### Row

Use `flex-row` to position flex items horizontally in the same direction as text:

<Figure>

<Example>
  {
    <div className="flex flex-row gap-x-4 font-mono text-sm leading-6 font-bold text-white">
      <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-fuchsia-500">01</div>
      <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-fuchsia-500">02</div>
      <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-fuchsia-500">03</div>
    </div>
  }
</Example>

```html
<!-- [!code classes:flex-row] -->
<div class="flex flex-row ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

</Figure>

### Row reversed

Use `flex-row-reverse` to position flex items horizontally in the opposite direction:

<Figure>

<Example>
  {
    <div className="flex flex-row-reverse gap-x-4 space-x-reverse font-mono text-sm leading-6 font-bold text-white">
      <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-blue-500">01</div>
      <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-blue-500">02</div>
      <div className="flex h-14 w-14 items-center justify-center rounded-lg bg-blue-500">03</div>
    </div>
  }
</Example>

```html
<!-- [!code classes:flex-row-reverse] -->
<div class="flex flex-row-reverse ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

</Figure>

### Column

Use `flex-col` to position flex items vertically:

<Figure>

<Example>
  {
    <div className="mx-auto flex max-w-xs flex-col space-y-4 font-mono text-sm leading-6 font-bold text-white">
      <div className="flex items-center justify-center rounded-lg bg-indigo-500 p-4">01</div>
      <div className="flex items-center justify-center rounded-lg bg-indigo-500 p-4">02</div>
      <div className="flex items-center justify-center rounded-lg bg-indigo-500 p-4">03</div>
    </div>
  }
</Example>

```html
<!-- [!code classes:flex-col] -->
<div class="flex flex-col ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

</Figure>

### Column reversed

Use `flex-col-reverse` to position flex items vertically in the opposite direction:

<Figure>

<Example>
  {
    <div className="mx-auto flex max-w-xs flex-col-reverse space-y-4 space-y-reverse font-mono text-sm leading-6 font-bold text-white">
      <div className="flex items-center justify-center rounded-lg bg-purple-500 p-4">01</div>
      <div className="flex items-center justify-center rounded-lg bg-purple-500 p-4">02</div>
      <div className="flex items-center justify-center rounded-lg bg-purple-500 p-4">03</div>
    </div>
  }
</Example>

```html
<!-- [!code classes:flex-col-reverse] -->
<div class="flex flex-col-reverse ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

</Figure>

### Responsive design

<ResponsiveDesign property="flex-direction" defaultClass="flex flex-col" featuredClass="flex-row" />
