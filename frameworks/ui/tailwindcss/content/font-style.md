---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/font-style.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.086770Z"
---
# Font Style

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "font-style";
export const description = "Utilities for controlling the style of text.";

<ApiTable
  rows={[
    ["italic", "font-style: italic;"],
    ["not-italic", "font-style: normal;"],
  ]}
/>

## Examples

### Italicizing text

Use the `italic` utility to make text italic:

<Figure>

<Example>
  {
    <p className="text-center text-lg font-medium text-gray-900 italic dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }
</Example>

```html
<!-- [!code classes:italic] -->
<p class="italic ...">The quick brown fox ...</p>
```

</Figure>

### Displaying text normally

Use the `not-italic` utility to display text normally:

<Figure>

<Example>
  {
    <p className="text-center text-lg font-medium text-gray-900 not-italic dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }
</Example>

```html
<!-- [!code classes:not-italic] -->
<p class="not-italic ...">The quick brown fox ...</p>
```

</Figure>

### Responsive design

<ResponsiveDesign property="font-style" defaultClass="italic" featuredClass="not-italic" element="p" />
