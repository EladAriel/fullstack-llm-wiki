---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/text-transform.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.747474Z"
---
# Text Transform

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "text-transform";
export const description = "Utilities for controlling the capitalization of text.";

<ApiTable
  rows={[
    ["uppercase", "text-transform: uppercase;"],
    ["lowercase", "text-transform: lowercase;"],
    ["capitalize", "text-transform: capitalize;"],
    ["normal-case", "text-transform: none;"],
  ]}
/>

## Examples

### Uppercasing text

Use the `uppercase` utility to uppercase the text of an element:

<Figure>

<Example>
  {
    <p className="text-center text-lg font-medium text-gray-900 uppercase dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }
</Example>

```html
<!-- [!code classes:uppercase] -->
<p class="uppercase">The quick brown fox ...</p>
```

</Figure>

### Lowercasing text

Use the `lowercase` utility to lowercase the text of an element:

<Figure>

<Example>
  {
    <p className="text-center text-lg font-medium text-gray-900 lowercase dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }
</Example>

```html
<!-- [!code classes:lowercase] -->
<p class="lowercase">The quick brown fox ...</p>
```

</Figure>

### Capitalizing text

Use the `capitalize` utility to capitalize text of an element:

<Figure>

<Example>
  {
    <p className="text-center text-lg font-medium text-gray-900 capitalize dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }
</Example>

```html
<!-- [!code classes:capitalize] -->
<p class="capitalize">The quick brown fox ...</p>
```

</Figure>

### Resetting text casing

Use the `normal-case` utility to preserve the original text casing of an element—typically used to reset capitalization at different breakpoints:

<Figure>

<Example>
  {
    <p className="text-center text-lg font-medium text-gray-900 normal-case dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }
</Example>

```html
<!-- [!code classes:normal-case] -->
<p class="normal-case">The quick brown fox ...</p>
```

</Figure>

### Responsive design

<ResponsiveDesign element="p" property="text-transform" defaultClass="capitalize" featuredClass="uppercase" />
