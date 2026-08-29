---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/text-underline-offset.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.753213Z"
---
# Text Underline Offset

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign, UsingACustomValue } from "@/components/content.tsx";

export const title = "text-underline-offset";
export const description = "Utilities for controlling the offset of a text underline.";

<ApiTable
  rows={[
    ["underline-offset-<number>", "text-underline-offset: <number>px;"],
    ["-underline-offset-<number>", "text-underline-offset: calc(<number>px * -1);"],
    ["underline-offset-auto", "text-underline-offset: auto;"],
    ["underline-offset-(<custom-property>)", "text-underline-offset: var(<custom-property>);"],
    ["underline-offset-[<value>]", "text-underline-offset: <value>;"],
  ]}
/>

## Examples

### Basic example

Use `underline-offset-<number>` utilities like `underline-offset-2` and `underline-offset-4` to change the offset of a text underline:

<Figure>

<Example>
  {
    <div className="flex flex-col gap-8 text-gray-900 dark:text-gray-200">
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">underline-offset-1</div>
        <p className="text-lg font-medium underline underline-offset-1">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">underline-offset-2</div>
        <p className="text-lg font-medium underline underline-offset-2">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">underline-offset-4</div>
        <p className="text-lg font-medium underline underline-offset-4">The quick brown fox jumps over the lazy dog.</p>
      </div>
      <div>
        <div className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">underline-offset-8</div>
        <p className="text-lg font-medium underline underline-offset-8">The quick brown fox jumps over the lazy dog.</p>
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:underline-offset-1] -->
<p class="underline underline-offset-1">The quick brown fox...</p>
<!-- [!code classes:underline-offset-2] -->
<p class="underline underline-offset-2">The quick brown fox...</p>
<!-- [!code classes:underline-offset-4] -->
<p class="underline underline-offset-4">The quick brown fox...</p>
<!-- [!code classes:underline-offset-8] -->
<p class="underline underline-offset-8">The quick brown fox...</p>
```

</Figure>

### Using a custom value

<UsingACustomValue element="p" utility="underline-offset" name="text underline offset" value="3px" />

### Responsive design

<ResponsiveDesign
  element="p"
  property="text-underline-offset"
  defaultClass="underline"
  featuredClass="underline-offset-4"
/>
