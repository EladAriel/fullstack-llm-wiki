---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/flex-wrap.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.726699Z"
---
# Flex Wrap

import { Stripes } from "@/components/stripes.tsx";
import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "flex-wrap";
export const description = "Utilities for controlling how flex items wrap.";

<ApiTable
  rows={[
    ["flex-nowrap", "flex-wrap: nowrap;"],
    ["flex-wrap", "flex-wrap: wrap;"],
    ["flex-wrap-reverse", "flex-wrap: wrap-reverse;"],
  ]}
/>

## Examples

### Don't wrap

Use `flex-nowrap` to prevent flex items from wrapping, causing inflexible items to overflow the container if necessary:

<Figure>

<Example>
  {
    <div className="grid grid-cols-1">
      <Stripes border className="col-start-1 row-start-1 rounded-lg" />
      <div className="col-start-1 row-start-1 flex flex-nowrap gap-4 rounded-lg font-mono text-sm/6 font-bold text-white">
        <div className="w-2/5 flex-none last:pr-8">
          <div className="flex w-full items-center justify-center rounded-lg bg-sky-500 p-4">01</div>
        </div>
        <div className="w-2/5 flex-none last:pr-8">
          <div className="flex w-full items-center justify-center rounded-lg bg-sky-500 p-4">02</div>
        </div>
        <div className="w-2/5 flex-none last:pr-8">
          <div className="flex w-full items-center justify-center rounded-lg bg-sky-500 p-4">03</div>
        </div>
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:flex-nowrap] -->
<div class="flex flex-nowrap">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

</Figure>

### Wrap normally

Use `flex-wrap` to allow flex items to wrap:

<Figure>

<Example>
  {
    <div className="grid grid-cols-1">
      <Stripes border className="col-start-1 row-start-1 rounded-lg" />
      <div className="col-start-1 row-start-1 flex flex-wrap gap-4 rounded-lg font-mono text-sm/6 font-bold text-white">
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-indigo-500 p-4">01</div>
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-indigo-500 p-4">02</div>
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-indigo-500 p-4">03</div>
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:flex-wrap] -->
<div class="flex flex-wrap">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

</Figure>

### Wrap reversed

Use `flex-wrap-reverse` to wrap flex items in the reverse direction:

<Figure>

<Example>
  {
    <div className="grid grid-cols-1">
      <Stripes border className="col-start-1 row-start-1 rounded-lg" />
      <div className="col-start-1 row-start-1 flex flex-wrap-reverse gap-4 rounded-lg font-mono text-sm/6 font-bold text-white">
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-fuchsia-500 p-4">01</div>
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-fuchsia-500 p-4">02</div>
        <div className="flex w-2/5 items-center justify-center rounded-lg bg-fuchsia-500 p-4">03</div>
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:flex-wrap-reverse] -->
<div class="flex flex-wrap-reverse">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

</Figure>

### Responsive design

<ResponsiveDesign property="flex-wrap" defaultClass="flex flex-wrap" featuredClass="flex-wrap-reverse" />
