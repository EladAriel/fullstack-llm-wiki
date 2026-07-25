---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/box-decoration-break.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.057096Z"
---
# Box Decoration Break

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "box-decoration-break";
export const description =
  "Utilities for controlling how element fragments should be rendered across multiple lines, columns, or pages.";

<ApiTable
  rows={[
    ["box-decoration-clone", "box-decoration-break: clone;"],
    ["box-decoration-slice", "box-decoration-break: slice;"],
  ]}
/>

## Examples

### Basic example

Use the `box-decoration-slice` and `box-decoration-clone` utilities to control whether properties like background, border, border-image, box-shadow, clip-path, margin, and padding should be rendered as if the element were one continuous fragment, or distinct blocks:

<Figure>

<Example>
  {
    <div className="grid grid-cols-1 gap-10 px-10 font-mono font-bold sm:grid-cols-2">
      <div className="flex flex-col">
        <p className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">box-decoration-slice</p>
        <div className="font-sans text-5xl leading-none font-extrabold tracking-tight">
          <span className="bg-linear-to-r from-indigo-600 to-pink-500 box-decoration-slice px-2 leading-14 text-white">
            Hello
            <br />
            World
          </span>
        </div>
      </div>
      <div className="flex flex-col">
        <p className="mb-3 font-mono text-xs font-medium text-gray-500 dark:text-gray-400">box-decoration-clone</p>
        <div className="font-sans text-5xl leading-none font-extrabold tracking-tight">
          <span className="bg-linear-to-r from-indigo-600 to-pink-500 box-decoration-clone px-2 leading-14 text-white">
            Hello
            <br />
            World
          </span>
        </div>
      </div>
    </div>
  }
</Example>

{/* prettier-ignore */}
```html
<!-- [!code classes:box-decoration-slice,box-decoration-clone] -->
<span class="box-decoration-slice bg-linear-to-r from-indigo-600 to-pink-500 px-2 text-white ...">
  Hello<br />World
</span>
<span class="box-decoration-clone bg-linear-to-r from-indigo-600 to-pink-500 px-2 text-white ...">
  Hello<br />World
</span>
```

</Figure>

### Responsive design

<ResponsiveDesign
  property="box-decoration-break"
  defaultClass="box-decoration-clone"
  featuredClass="box-decoration-slice"
/>
