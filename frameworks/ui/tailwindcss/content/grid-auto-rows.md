---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/grid-auto-rows.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.100668Z"
---
# Grid Auto Rows

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign, UsingACustomValue } from "@/components/content.tsx";

export const title = "grid-auto-rows";
export const description = "Utilities for controlling the size of implicitly-created grid rows.";

<ApiTable
  rows={[
    ["auto-rows-auto", "grid-auto-rows: auto;"],
    ["auto-rows-min", "grid-auto-rows: min-content;"],
    ["auto-rows-max", "grid-auto-rows: max-content;"],
    ["auto-rows-fr", "grid-auto-rows: minmax(0, 1fr);"],
    ["auto-rows-<number>", "grid-auto-rows: calc(var(--spacing) * <number>);"],
    ["auto-rows-(<custom-property>)", "grid-auto-rows: var(<custom-property>);"],
    ["auto-rows-[<value>]", "grid-auto-rows: <value>;"],
  ]}
/>

## Examples

### Basic example

Use utilities like `auto-rows-min` and `auto-rows-max` to control the size of implicitly-created grid rows:

```html
<!-- [!code classes:auto-rows-max] -->
<div class="grid grid-flow-row auto-rows-max">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

### Using a custom value

<UsingACustomValue utility="auto-rows" name="size of implicitly-created grid rows" value="minmax(0,2fr)" />

### Responsive design

<ResponsiveDesign
  property="grid-auto-rows"
  defaultClass="grid grid-flow-row auto-rows-max"
  featuredClass="auto-rows-min"
/>
