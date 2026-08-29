---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/list-style-type.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.744844Z"
---
# List Style Type

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign, UsingACustomValue } from "@/components/content.tsx";

export const title = "list-style-type";
export const description = "Utilities for controlling the marker style of a list.";

<ApiTable
  rows={[
    ["list-disc", "list-style-type: disc;"],
    ["list-decimal", "list-style-type: decimal;"],
    ["list-none", "list-style-type: none;"],
    ["list-(<custom-property>)", "list-style-type: var(<custom-property>);"],
    ["list-[<value>]", "list-style-type: <value>;"],
  ]}
/>

## Examples

### Basic example

Use utilities like `list-disc` and `list-decimal` to control the style of the markers in a list:

<Figure>

<Example>
  {
    <div className="flex flex-col gap-8">
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">list-disc</span>
        <ul className="list-inside list-disc text-gray-900 dark:text-gray-200">
          <li>Now this is a story all about how, my life got flipped-turned upside down</li>
          <li>And I'd like to take a minute just sit right there</li>
          <li>I'll tell you how I became the prince of a town called Bel-Air</li>
        </ul>
      </div>
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">list-decimal</span>
        <ul className="list-inside list-decimal text-gray-900 dark:text-gray-200">
          <li>Now this is a story all about how, my life got flipped-turned upside down</li>
          <li>And I'd like to take a minute just sit right there</li>
          <li>I'll tell you how I became the prince of a town called Bel-Air</li>
        </ul>
      </div>
      <div>
        <span className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">list-none</span>
        <ul className="list-inside list-none text-gray-900 dark:text-gray-200">
          <li>Now this is a story all about how, my life got flipped-turned upside down</li>
          <li>And I'd like to take a minute just sit right there</li>
          <li>I'll tell you how I became the prince of a town called Bel-Air</li>
        </ul>
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:list-disc] -->
<ul class="list-disc">
  <li>Now this is a story all about how, my life got flipped-turned upside down</li>
  <!-- ... -->
</ul>

<!-- [!code classes:list-decimal] -->
<ol class="list-decimal">
  <li>Now this is a story all about how, my life got flipped-turned upside down</li>
  <!-- ... -->
</ol>

<!-- [!code classes:list-none] -->
<ul class="list-none">
  <li>Now this is a story all about how, my life got flipped-turned upside down</li>
  <!-- ... -->
</ul>
```

</Figure>

### Using a custom value

<UsingACustomValue element="ol" utility="list" name="marker" value="upper-roman" variable="marker" />

### Responsive design

<ResponsiveDesign element="ul" property="list-style-type" defaultClass="list-none" featuredClass="list-disc" />
