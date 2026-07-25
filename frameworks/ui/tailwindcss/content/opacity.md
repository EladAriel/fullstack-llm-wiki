---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/opacity.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.086423Z"
---
# Opacity

import { ApiTable } from "@/components/api-table.tsx";
import { CustomizingYourTheme, ResponsiveDesign, UsingACustomValue } from "@/components/content.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { TargetingSpecificStates } from "@/components/content.tsx";

export const title = "opacity";
export const description = "Utilities for controlling the opacity of an element.";

<ApiTable
  rows={[
    ["opacity-<number>", "opacity: <number>%;"],
    ["opacity-(<custom-property>)", "opacity: var(<custom-property>);"],
    ["opacity-[<value>]", "opacity: <value>;"],
  ]}
/>

## Examples

### Basic example

Use `opacity-<number>` utilities like `opacity-25` and `opacity-100` to set the opacity of an element:

<Figure>

<Example>
  {
    <div className="flex flex-col items-center justify-center gap-8 text-sm leading-6 font-bold text-white sm:flex-row sm:gap-16">
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">opacity-100</p>
        <button className="rounded-md bg-indigo-500 px-4 py-2 text-sm font-semibold text-white opacity-100">
          Button A
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">opacity-75</p>
        <button className="rounded-md bg-indigo-500 px-4 py-2 text-sm font-semibold text-white opacity-75">
          Button B
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">opacity-50</p>
        <button className="rounded-md bg-indigo-500 px-4 py-2 text-sm font-semibold text-white opacity-50">
          Button C
        </button>
      </div>
      <div className="flex shrink-0 flex-col items-center">
        <p className="mb-3 text-center font-mono text-xs font-medium text-gray-500 dark:text-gray-400">opacity-25</p>
        <button className="rounded-md bg-indigo-500 px-4 py-2 text-sm font-semibold text-white opacity-25">
          Button D
        </button>
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:opacity-100,opacity-75,opacity-50,opacity-25] -->
<button class="bg-indigo-500 opacity-100 ..."></button>
<button class="bg-indigo-500 opacity-75 ..."></button>
<button class="bg-indigo-500 opacity-50 ..."></button>
<button class="bg-indigo-500 opacity-25 ..."></button>
```

</Figure>

### Applying conditionally

<TargetingSpecificStates
  element="input"
  elementAttributes={{ type: "text" }}
  variant="disabled"
  property="opacity"
  defaultClass="opacity-100"
  featuredClass="opacity-75"
/>

### Using a custom value

<UsingACustomValue element="button" utility="opacity" value=".67" />

### Responsive design

<ResponsiveDesign element="button" property="opacity" defaultClass="opacity-50" featuredClass="opacity-100" />
