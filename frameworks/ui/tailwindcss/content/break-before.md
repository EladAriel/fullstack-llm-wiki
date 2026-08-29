---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/break-before.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.756713Z"
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
