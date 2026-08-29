---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/font-smoothing.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.749765Z"
---
# Font Smoothing

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "font-smoothing";
export const description = "Utilities for controlling the font smoothing of an element.";

<ApiTable
  rows={[
    ["antialiased", "-webkit-font-smoothing: antialiased;\n-moz-osx-font-smoothing: grayscale;"],
    ["subpixel-antialiased", "-webkit-font-smoothing: auto;\n-moz-osx-font-smoothing: auto;"],
  ]}
/>

## Examples

### Grayscale antialiasing

Use the `antialiased` utility to render text using grayscale antialiasing:

<Figure>

<Example>
  {
    <p className="text-center text-lg font-medium text-gray-900 antialiased dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }
</Example>

```html
<!-- [!code classes:antialiased] -->
<p class="antialiased ...">The quick brown fox ...</p>
```

</Figure>

### Subpixel antialiasing

Use the `subpixel-antialiased` utility to render text using subpixel antialiasing:

<Figure>

<Example>
  {
    <p className="text-center text-lg font-medium text-gray-900 subpixel-antialiased dark:text-gray-200">
      The quick brown fox jumps over the lazy dog.
    </p>
  }
</Example>

```html
<!-- [!code classes:subpixel-antialiased] -->
<p class="subpixel-antialiased ...">The quick brown fox ...</p>
```

</Figure>

### Responsive design

<ResponsiveDesign
  element="p"
  properties={["-webkit-font-smoothing", "-moz-osx-font-smoothing"]}
  defaultClass="antialiased"
  featuredClass="subpixel-antialiased"
/>
