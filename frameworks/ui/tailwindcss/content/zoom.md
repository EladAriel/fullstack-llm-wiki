---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/zoom.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.062775Z"
---
# Zoom

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign, TargetingSpecificStates, UsingACustomValue } from "@/components/content.tsx";

export const title = "zoom";
export const description = "Utilities for scaling elements using zoom.";

<ApiTable
  rows={[
    ["zoom-<number>", "zoom: <number>%;"],
    ["zoom-(<custom-property>)", "zoom: var(<custom-property>);"],
    ["zoom-[<value>]", "zoom: <value>;"],
  ]}
/>

## Examples

### Basic example

Use `zoom-<number>` utilities like `zoom-75` and `zoom-125` to scale an element using the CSS `zoom` property:

```html
<!-- [!code classes:zoom-75,zoom-100,zoom-125] -->
<div class="zoom-75 ...">
  <!-- ... -->
</div>
<div class="zoom-100 ...">
  <!-- ... -->
</div>
<div class="zoom-125 ...">
  <!-- ... -->
</div>
```

### Using a custom value

<UsingACustomValue utility="zoom" value="1.1" />

### Applying on hover

<TargetingSpecificStates property="zoom" defaultClass="zoom-100" featuredClass="zoom-125" />

### Responsive design

<ResponsiveDesign property="zoom" defaultClass="zoom-100" featuredClass="zoom-125" />
