---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/grid-auto-columns.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.069545Z"
---
# Grid Auto Columns

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign, UsingACustomValue } from "@/components/content.tsx";

export const title = "grid-auto-columns";
export const description = "Utilities for controlling the size of implicitly-created grid columns.";

<ApiTable
  rows={[
    ["auto-cols-auto", "grid-auto-columns: auto;"],
    ["auto-cols-min", "grid-auto-columns: min-content;"],
    ["auto-cols-max", "grid-auto-columns: max-content;"],
    ["auto-cols-fr", "grid-auto-columns: minmax(0, 1fr);"],
    ["auto-cols-<number>", "grid-auto-columns: calc(var(--spacing) * <number>);"],
    ["auto-cols-(<custom-property>)", "grid-auto-columns: var(<custom-property>);"],
    ["auto-cols-[<value>]", "grid-auto-columns: <value>;"],
  ]}
/>

## Examples

### Basic example

Use utilities like `auto-cols-min` and `auto-cols-max` to control the size of implicitly-created grid columns:

```html
<!-- [!code classes:auto-cols-max] -->
<div class="grid auto-cols-max grid-flow-col">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Using a custom value

<UsingACustomValue utility="auto-cols" name="size of implicitly-created grid columns" value="minmax(0,2fr)" />

### Responsive design

<ResponsiveDesign
  property="grid-auto-columns"
  defaultClass="grid grid-flow-col auto-cols-max"
  featuredClass="auto-cols-min"
/>
