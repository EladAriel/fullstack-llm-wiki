---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/isolation.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.763136Z"
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
