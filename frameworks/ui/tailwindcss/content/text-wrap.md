---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/text-wrap.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.094918Z"
---
# Text Wrap

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { ResponsiveDesign } from "@/components/content.tsx";

export const title = "text-wrap";
export const description = "Utilities for controlling how text wraps within an element.";

<ApiTable
  rows={[
    ["text-wrap", "text-wrap: wrap;"],
    ["text-nowrap", "text-wrap: nowrap;"],
    ["text-balance", "text-wrap: balance;"],
    ["text-pretty", "text-wrap: pretty;"],
  ]}
/>

## Examples

### Allowing text to wrap

Use the `text-wrap` utility to wrap overflowing text onto multiple lines at logical points in the text:

<Figure>

<Example padding={false}>
  {
    <div className="mx-auto grid max-w-xs gap-4 border-x border-x-pink-400/30 py-8 text-gray-700 dark:text-gray-400">
      <div className="text-xl font-semibold text-gray-900 dark:text-white">Beloved Manhattan soup stand closes</div>
      <p className="text-sm/6">
        New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand
        unexpectedly shutters, following a series of events that have left the community puzzled.
      </p>
    </div>
  }
</Example>

```html
<!-- [!code classes:text-wrap] -->
<article class="text-wrap">
  <h3>Beloved Manhattan soup stand closes</h3>
  <p>New Yorkers are facing the winter chill...</p>
</article>
```

</Figure>

### Preventing text from wrapping

Use the `text-nowrap` utility to prevent text from wrapping, allowing it to overflow if necessary:

<Figure>

<Example padding={false}>
  {
    <div className="overflow-hidden">
      <div className="mx-auto grid max-w-xs gap-4 border-x border-x-pink-400/30 py-8 text-gray-700 dark:text-gray-400">
        <div className="text-xl font-semibold text-nowrap text-gray-900 dark:text-white">
          Beloved Manhattan soup stand closes
        </div>
        <p className="text-sm/6 text-nowrap">
          New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand
          unexpectedly shutters, following a series of events that have left the community puzzled.
        </p>
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:text-nowrap] -->
<article class="text-nowrap">
  <h3>Beloved Manhattan soup stand closes</h3>
  <p>New Yorkers are facing the winter chill...</p>
</article>
```

</Figure>

### Balanced text wrapping

Use the `text-balance` utility to distribute the text evenly across each line:

<Figure>

<Example padding={false}>
  {
    <div className="mx-auto grid max-w-xs gap-4 border-x border-x-pink-400/30 py-8 text-gray-700 dark:text-gray-400">
      <div className="text-xl font-semibold text-balance text-gray-900 dark:text-white">
        Beloved Manhattan soup stand closes
      </div>
      <p className="text-sm/6">
        New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand
        unexpectedly shutters, following a series of events that have left the community puzzled.
      </p>
    </div>
  }
</Example>

```html
<!-- [!code classes:text-balance] -->
<article>
  <h3 class="text-balance">Beloved Manhattan soup stand closes</h3>
  <p>New Yorkers are facing the winter chill...</p>
</article>
```

</Figure>

For performance reasons browsers limit text balancing to blocks that are ~6 lines or less, making it best suited for headings.

### Pretty text wrapping

Use the `text-pretty` utility to prefer better text wrapping and layout at the expense of speed. Behavior varies across browsers but often involves approaches like preventing orphans (a single word on its own line) at the end of a text block:

<Figure>

<Example padding={false}>
  {
    <div className="mx-auto grid max-w-xs gap-4 border-x border-x-pink-400/30 py-8 text-gray-700 dark:text-gray-400">
      <div className="text-xl font-semibold text-pretty text-gray-900 dark:text-white">
        Beloved Manhattan soup stand closes
      </div>
      <p className="text-sm/6">
        New Yorkers are facing the winter chill with less warmth this year as the city's most revered soup stand
        unexpectedly shutters, following a series of events that have left the community puzzled.
      </p>
    </div>
  }
</Example>

```html
<!-- [!code classes:text-pretty] -->
<article>
  <h3 class="text-pretty">Beloved Manhattan soup stand closes</h3>
  <p>New Yorkers are facing the winter chill...</p>
</article>
```

</Figure>

### Responsive design

<ResponsiveDesign element="h1" property="text-wrap" defaultClass="text-pretty" featuredClass="text-balance" />
