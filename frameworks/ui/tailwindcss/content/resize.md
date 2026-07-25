---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/resize.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.106133Z"
---
# Resize

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "resize";
export const description = "Utilities for controlling how an element can be resized.";

<ApiTable
  rows={[
    ["resize-none", "resize: none;"],
    ["resize", "resize: both;"],
    ["resize-y", "resize: vertical;"],
    ["resize-x", "resize: horizontal;"],
  ]}
/>

## Examples

### Resizing in all directions

Use `resize` to make an element horizontally and vertically resizable:

<Figure hint="Drag the textarea handle in the demo to see the expected behavior">

<Example>
  {
    <textarea
      rows="2"
      className="mx-auto block w-80 resize rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    ></textarea>
  }
</Example>

```html
<!-- [!code classes:resize] -->
<textarea class="resize rounded-md ..."></textarea>
```

</Figure>

### Resizing vertically

Use `resize-y` to make an element vertically resizable:

<Figure hint="Drag the textarea handle in the demo to see the expected behavior">

<Example>
  {
    <textarea
      rows="2"
      className="mx-auto block w-80 resize-y rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    ></textarea>
  }
</Example>

```html
<!-- [!code classes:resize-y] -->
<textarea class="resize-y rounded-md ..."></textarea>
```

</Figure>

### Resizing horizontally

Use `resize-x` to make an element horizontally resizable:

<Figure hint="Drag the textarea handle in the demo to see the expected behavior">

<Example>
  {
    <textarea
      rows="2"
      className="mx-auto block w-80 resize-x rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    ></textarea>
  }
</Example>

```html
<!-- [!code classes:resize-x] -->
<textarea class="resize-x rounded-md ..."></textarea>
```

</Figure>

### Prevent resizing

Use `resize-none` to prevent an element from being resizable:

<Figure hint="Notice that the textarea handle is gone">

<Example>
  {
    <textarea
      rows="2"
      className="mx-auto block w-80 resize-none rounded-md p-2 text-sm text-gray-950 outline-1 outline-gray-900/10 focus:outline-2 focus:outline-gray-900 dark:bg-gray-950/25 dark:text-white dark:outline-1 dark:outline-white/5 dark:focus:outline-white/20"
    ></textarea>
  }
</Example>

```html
<!-- [!code classes:resize-none] -->
<textarea class="resize-none rounded-md"></textarea>
```

</Figure>

### Responsive design

<ResponsiveDesign property="resize" defaultClass="resize-none" featuredClass="resize" />
