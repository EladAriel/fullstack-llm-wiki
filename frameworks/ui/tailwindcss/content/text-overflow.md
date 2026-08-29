---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/text-overflow.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.743343Z"
---
# Text Overflow

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";
import dedent from "dedent";

export const title = "text-overflow";
export const description = "Utilities for controlling how the text of an element overflows.";

<ApiTable
  rows={[
    [
      "truncate",
      dedent`
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      `,
    ],
    ["text-ellipsis", "text-overflow: ellipsis;"],
    ["text-clip", "text-overflow: clip;"],
  ]}
/>

## Examples

### Truncating text

Use the `truncate` utility to prevent text from wrapping and truncate overflowing text with an ellipsis (…) if needed:

<Figure>

<Example padding={false}>
  {
    <p className="mx-auto max-w-xs truncate border-x border-x-pink-400/30 py-8 text-gray-900 dark:text-gray-200">
      The longest word in any of the major English language dictionaries is{" "}
      <span className="font-bold">pneumonoultramicroscopicsilicovolcanoconiosis,</span> a word that refers to a lung
      disease contracted from the inhalation of very fine silica particles, specifically from a volcano; medically, it
      is the same as silicosis.
    </p>
  }
</Example>

```html
<!-- [!code classes:truncate] -->
<p class="truncate">The longest word in any of the major...</p>
```

</Figure>

### Adding an ellipsis

Use the `text-ellipsis` utility to truncate overflowing text with an ellipsis (…) if needed:

<Figure>

<Example padding={false}>
  {
    <p className="mx-auto max-w-xs overflow-hidden border-x border-x-pink-400/30 py-8 text-ellipsis text-gray-900 dark:text-gray-200">
      The longest word in any of the major English language dictionaries is{" "}
      <span className="font-bold">pneumonoultramicroscopicsilicovolcanoconiosis,</span> a word that refers to a lung
      disease contracted from the inhalation of very fine silica particles, specifically from a volcano; medically, it
      is the same as silicosis.
    </p>
  }
</Example>

```html
<!-- [!code classes:text-ellipsis] -->
<p class="overflow-hidden text-ellipsis">The longest word in any of the major...</p>
```

</Figure>

### Clipping text

Use the `text-clip` utility to truncate the text at the limit of the content area:

<Figure>

<Example padding={false}>
  {
    <p className="mx-auto max-w-xs overflow-hidden border-x border-x-pink-400/30 py-8 text-clip text-gray-900 dark:text-gray-200">
      The longest word in any of the major English language dictionaries is{" "}
      <span className="font-bold">pneumonoultramicroscopicsilicovolcanoconiosis,</span> a word that refers to a lung
      disease contracted from the inhalation of very fine silica particles, specifically from a volcano; medically, it
      is the same as silicosis.
    </p>
  }
</Example>

```html
<!-- [!code classes:text-clip] -->
<p class="overflow-hidden text-clip">The longest word in any of the major...</p>
```

</Figure>

This is the default browser behavior.

### Responsive design

<ResponsiveDesign element="p" property="text-overflow" defaultClass="text-ellipsis" featuredClass="text-clip" />
