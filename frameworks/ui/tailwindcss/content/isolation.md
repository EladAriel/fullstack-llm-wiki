---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/isolation.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.104426Z"
---
# Isolation

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "isolation";
export const description =
  "Utilities for controlling whether an element should explicitly create a new stacking context.";

<ApiTable
  rows={[
    ["isolate", "isolation: isolate;"],
    ["isolation-auto", "isolation: auto;"],
  ]}
/>

## Examples

### Basic example

Use the `isolate` and `isolation-auto` utilities to control whether an element should explicitly create a new stacking context:

```html
<!-- [!code classes:isolate] -->
<div class="isolate ...">
  <!-- ... -->
</div>
```

### Responsive design

<ResponsiveDesign property="isolation" defaultClass="isolate" featuredClass="isolation-auto" />
