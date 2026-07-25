---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/break-inside.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.100349Z"
---
# Break Inside

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "break-inside";
export const description = "Utilities for controlling how a column or page should break within an element.";

<ApiTable
  rows={[
    ["break-inside-auto", "break-inside: auto;"],
    ["break-inside-avoid", "break-inside: avoid;"],
    ["break-inside-avoid-page", "break-inside: avoid-page;"],
    ["break-inside-avoid-column", "break-inside: avoid-column;"],
  ]}
/>

## Examples

### Basic example

Use utilities like `break-inside-column` and `break-inside-avoid-page` to control how a column or page break should behave within an element:

```html
<!-- [!code classes:break-inside-avoid-column] -->
<div class="columns-2">
  <p>Well, let me tell you something, ...</p>
  <p class="break-inside-avoid-column">Sure, go ahead, laugh...</p>
  <p>Maybe we can live without...</p>
  <p>Look. If you think this is...</p>
</div>
```

### Responsive design

<ResponsiveDesign property="break-inside" defaultClass="break-inside-avoid-column" featuredClass="break-inside-auto" />
