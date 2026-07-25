---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/text-indent.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.103070Z"
---
# Text Indent

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign, UsingACustomValue } from "@/components/content.tsx";

export const title = "text-indent";
export const description = "Utilities for controlling the amount of empty space shown before text in a block.";

<ApiTable
  rows={[
    ["indent-<number>", "text-indent: calc(var(--spacing) * <number>);"],
    ["-indent-<number>", "text-indent: calc(var(--spacing) * -<number>);"],
    ["indent-px", "text-indent: 1px;"],
    ["-indent-px", "text-indent: -1px;"],
    ["indent-(<custom-property>)", "text-indent: var(<custom-property>);"],
    ["indent-[<value>]", "text-indent: <value>;"],
  ]}
/>

## Examples

### Basic example

Use `indent-<number>` utilities like `indent-2` and `indent-8` to set the amount of empty space (indentation) that's shown before text in a block:

<Figure>

<Example>
  {
    <p className="mx-auto max-w-sm indent-8 text-gray-900 dark:text-gray-200">
      So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my
      way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of
      all living things but I tell you Jerry at that moment, I <em>was</em> a marine biologist.
    </p>
  }
</Example>

```html
<!-- [!code classes:indent-8] -->
<p class="indent-8">So I started to walk into the water...</p>
```

</Figure>

### Using negative values

To use a negative text indent value, prefix the class name with a dash to convert it to a negative value:

<Figure>

<Example>
  {
    <p className="mx-auto max-w-sm -indent-8 text-gray-900 dark:text-gray-200">
      So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my
      way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of
      all living things but I tell you Jerry at that moment, I <em>was</em> a marine biologist.
    </p>
  }
</Example>

```html
<!-- [!code classes:-indent-8] -->
<p class="-indent-8">So I started to walk into the water...</p>
```

</Figure>

### Using a custom value

<UsingACustomValue element="p" utility="indent" name="text indentation" value="50%" variable="indentation" />

### Responsive design

<ResponsiveDesign element="p" property="text-indent" defaultClass="indent-4" featuredClass="indent-8" />
