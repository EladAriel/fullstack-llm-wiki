---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/transform.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.066435Z"
---
# Transform

import { ApiTable } from "@/components/api-table.tsx";
import { UsingACustomValue } from "@/components/content.tsx";

export const title = "transform";
export const description = "Utilities for transforming elements.";

<ApiTable
  rows={[
    ["transform-(<custom-property>)", "transform: var(<custom-property>);"],
    ["transform-[<value>]", "transform: <value>;"],
    ["transform-none", "transform: none;"],
    [
      "transform-gpu",
      "transform: translateZ(0) var(--tw-rotate-x) var(--tw-rotate-y) var(--tw-rotate-z) var(--tw-skew-x) var(--tw-skew-y);",
    ],
    [
      "transform-cpu",
      "transform: var(--tw-rotate-x) var(--tw-rotate-y) var(--tw-rotate-z) var(--tw-skew-x) var(--tw-skew-y);",
    ],
  ]}
/>

## Examples

### Hardware acceleration

If your transition performs better when rendered by the GPU instead of the CPU, you can force hardware acceleration by adding the `transform-gpu` utility:

```html
<!-- [!code classes:transform-gpu] -->
<div class="scale-150 transform-gpu">
  <!-- ... -->
</div>
```

Use the `transform-cpu` utility to force things back to the CPU if you need to undo this conditionally.

### Removing transforms

Use the `transform-none` utility to remove all of the transforms on an element at once:

```html
<!-- [!code classes:transform-none] -->
<div class="skew-y-3 md:transform-none">
  <!-- ... -->
</div>
```

### Using a custom value

<UsingACustomValue utility="transform" value="matrix(1,2,3,4,5,6)" />
