---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/break-after.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.739910Z"
---
# Break After

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "break-after";
export const description = "Utilities for controlling how a column or page should break after an element.";

<ApiTable
  rows={[
    ["break-after-auto", "break-after: auto;"],
    ["break-after-avoid", "break-after: avoid;"],
    ["break-after-all", "break-after: all;"],
    ["break-after-avoid-page", "break-after: avoid-page;"],
    ["break-after-page", "break-after: page;"],
    ["break-after-left", "break-after: left;"],
    ["break-after-right", "break-after: right;"],
    ["break-after-column", "break-after: column;"],
  ]}
/>

## Examples

### Basic example

Use utilities like `break-after-column` and `break-after-page` to control how a column or page break should behave after an element:

```html
<!-- [!code classes:break-after-column] -->
<div class="columns-2">
  <p>Well, let me tell you something, ...</p>
  <p class="break-after-column">Sure, go ahead, laugh...</p>
  <p>Maybe we can live without...</p>
  <p>Look. If you think this is...</p>
</div>
```

### Responsive design

<ResponsiveDesign property="break-after" defaultClass="break-after-column" featuredClass="break-after-auto" />
