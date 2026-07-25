---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/tab-size.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.117036Z"
---
# Tab Size

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign, UsingACustomValue } from "@/components/content.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";

export const title = "tab-size";
export const description = "Utilities for controlling the size of tab characters.";

<ApiTable
  rows={[
    ["tab-<number>", "tab-size: <number>;"],
    ["tab-(<custom-property>)", "tab-size: var(<custom-property>);"],
    ["tab-[<value>]", "tab-size: <value>;"],
  ]}
/>

## Examples

### Basic example

Use `tab-<number>` utilities like `tab-2` and `tab-8` to control the size of tab characters:

<Figure>

<Example>
  <div className="grid gap-6 sm:grid-cols-2">
    <div className="tab-2">
      <span className="mb-3 block font-mono text-xs font-medium text-gray-500 dark:text-gray-400">tab-2</span>

{/* prettier-ignore */}
```jsx
function indent() {
	return 'tabbed';
}
```

    </div>
    <div className="tab-8">
      <span className="mb-3 block font-mono text-xs font-medium text-gray-500 dark:text-gray-400">tab-8</span>

{/* prettier-ignore */}
```jsx
function indent() {
	return 'tabbed';
}
```

    </div>

  </div>
</Example>

```html
<!-- [!code classes:tab-2,tab-8] -->
<pre class="tab-2 ...">function indent() {&#10;&#9;return 'tabbed'&#10;}</pre>
<pre class="tab-8 ...">function indent() {&#10;&#9;return 'tabbed'&#10;}</pre>
```

</Figure>

### Using a custom value

<UsingACustomValue element="pre" utility="tab" name="tab size" value="12px" variable="tab-size" />

### Responsive design

<ResponsiveDesign element="pre" property="tab-size" defaultClass="tab-4" featuredClass="tab-8" />
