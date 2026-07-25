---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/break-before.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.082770Z"
---
# Break Before

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "break-before";
export const description = "Utilities for controlling how a column or page should break before an element.";

<ApiTable
  rows={[
    ["break-before-auto", "break-before: auto;"],
    ["break-before-avoid", "break-before: avoid;"],
    ["break-before-all", "break-before: all;"],
    ["break-before-avoid-page", "break-before: avoid-page;"],
    ["break-before-page", "break-before: page;"],
    ["break-before-left", "break-before: left;"],
    ["break-before-right", "break-before: right;"],
    ["break-before-column", "break-before: column;"],
  ]}
/>

## Examples

### Basic example

Use utilities like `break-before-column` and `break-before-page` to control how a column or page break should behave before an element:

```html
<!-- [!code classes:break-before-column] -->
<div class="columns-2">
  <p>Well, let me tell you something, ...</p>
  <p class="break-before-column">Sure, go ahead, laugh...</p>
  <p>Maybe we can live without...</p>
  <p>Look. If you think this is...</p>
</div>
```

### Responsive design

<ResponsiveDesign property="break-before" defaultClass="break-before-column" featuredClass="break-before-auto" />
