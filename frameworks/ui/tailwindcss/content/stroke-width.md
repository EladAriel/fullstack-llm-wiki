---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/stroke-width.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.728295Z"
---
# Stroke Width

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign, UsingACustomValue } from "@/components/content.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";

export const title = "stroke-width";
export const description = "Utilities for styling the stroke width of SVG elements.";

<ApiTable
  rows={[
    ["stroke-<number>", "stroke-width: <number>;"],
    ["stroke-(length:<custom-property>)", "stroke-width: var(<custom-property>);"],
    ["stroke-[<value>]", "stroke-width: <value>;"],
  ]}
/>

## Examples

### Basic example

Use `stroke-<number>` utilities like `stroke-1` and `stroke-2` to set the stroke width of an SVG:

<Figure>

<Example>
  {
    <div className="flex items-center justify-center gap-x-8">
      <svg
        className="stroke-indigo-500 stroke-1"
        width="48"
        height="48"
        viewBox="0 0 48 48"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle cx="24" cy="24" r="23" strokeLinejoin="round" />
        <path d="M23 1C23 1 15 10.4901 15 24C15 37.5099 23 47 23 47" strokeLinejoin="round" />
        <path d="M25 1C25 1 33 10.4901 33 24C33 37.5099 25 47 25 47" strokeLinejoin="round" />
        <path d="M1 24H47" />
      </svg>
      <svg
        className="stroke-indigo-500 stroke-2"
        width="48"
        height="48"
        viewBox="0 0 48 48"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle cx="24" cy="24" r="23" strokeLinejoin="round" />
        <path d="M23 1C23 1 15 10.4901 15 24C15 37.5099 23 47 23 47" strokeLinejoin="round" />
        <path d="M25 1C25 1 33 10.4901 33 24C33 37.5099 25 47 25 47" strokeLinejoin="round" />
        <path d="M1 24H47" />
      </svg>
    </div>
  }
</Example>

```html
<!-- [!code classes:stroke-1,stroke-2] -->
<svg class="stroke-1 ..."></svg>
<svg class="stroke-2 ..."></svg>
```

</Figure>

This can be useful for styling icon sets like [Heroicons](https://heroicons.com).

### Using a custom value

<UsingACustomValue utility="stroke" name="stroke width" value="1.5" variable="stroke-width" dataType="length" />

### Responsive design

<ResponsiveDesign property="stroke-width" defaultClass="stroke-1" featuredClass="stroke-2" />
