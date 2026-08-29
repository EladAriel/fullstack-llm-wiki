---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/user-select.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.758874Z"
---
# User Select

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "user-select";
export const description = "Utilities for controlling whether the user can select text in an element.";

<ApiTable
  rows={[
    ["select-none", "user-select: none;"],
    ["select-text", "user-select: text;"],
    ["select-all", "user-select: all;"],
    ["select-auto", "user-select: auto;"],
  ]}
/>

## Examples

### Disabling text selection

Use the `select-none` utility to prevent selecting text in an element and its children:

<Figure hint="Try selecting the text to see the expected behavior">

<Example>
  {
    <div className="flex justify-center">
      <div className="dark:highlight-white/5 inline-flex rounded-lg bg-white px-4 py-3 text-center font-sans text-sm font-semibold text-gray-900 ring-1 ring-gray-900/5 select-none dark:bg-gray-800 dark:text-gray-200 dark:ring-0">
        The quick brown fox jumps over the lazy dog.
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:select-none] -->
<div class="select-none ...">The quick brown fox jumps over the lazy dog.</div>
```

</Figure>

### Allowing text selection

Use the `select-text` utility to allow selecting text in an element and its children:

<Figure hint="Try selecting the text to see the expected behavior">

<Example>
  {
    <div className="flex justify-center">
      <div className="dark:highlight-white/5 inline-flex rounded-lg bg-white px-4 py-3 text-center font-sans text-sm font-semibold text-gray-900 ring-1 ring-gray-900/5 select-text dark:bg-gray-800 dark:text-gray-200 dark:ring-0">
        The quick brown fox jumps over the lazy dog.
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:select-text] -->
<div class="select-text ...">The quick brown fox jumps over the lazy dog.</div>
```

</Figure>

### Selecting all text in one click

Use the `select-all` utility to automatically select all the text in an element when a user clicks:

<Figure hint="Try clicking the text to see the expected behavior">

<Example>
  {
    <div className="flex justify-center">
      <div className="dark:highlight-white/5 inline-flex rounded-lg bg-white px-4 py-3 text-center font-sans text-sm font-semibold text-gray-900 ring-1 ring-gray-900/5 select-all dark:bg-gray-800 dark:text-gray-200 dark:ring-0">
        The quick brown fox jumps over the lazy dog.
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:select-all] -->
<div class="select-all ...">The quick brown fox jumps over the lazy dog.</div>
```

</Figure>

### Using auto select behavior

Use the `select-auto` utility to use the default browser behavior for selecting text:

<Figure hint="Try selecting the text to see the expected behavior">

<Example>
  {
    <div className="flex justify-center">
      <div className="dark:highlight-white/5 inline-flex rounded-lg bg-white px-4 py-3 text-center font-sans text-sm font-semibold text-gray-900 ring-1 ring-gray-900/5 select-auto dark:bg-gray-800 dark:text-gray-200 dark:ring-0">
        The quick brown fox jumps over the lazy dog.
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:select-auto] -->
<div class="select-auto ...">The quick brown fox jumps over the lazy dog.</div>
```

</Figure>

### Responsive design

<ResponsiveDesign property="user-select" defaultClass="select-none" featuredClass="select-all" />
