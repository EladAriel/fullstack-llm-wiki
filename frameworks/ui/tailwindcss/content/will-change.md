---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/will-change.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.093231Z"
---
# Will Change

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { UsingACustomValue } from "@/components/content.tsx";

export const title = "will-change";
export const description = "Utilities for optimizing upcoming animations of elements that are expected to change.";

<ApiTable
  rows={[
    ["will-change-auto", "will-change: auto;"],
    ["will-change-scroll", "will-change: scroll-position;"],
    ["will-change-contents", "will-change: contents;"],
    ["will-change-transform", "will-change: transform;"],
    ["will-change-<custom-property>", "will-change: var(<custom-property>);"],
    ["will-change-[<value>]", "will-change: <value>;"],
  ]}
/>

## Examples

### Optimizing with will change

Use the `will-change-scroll`, `will-change-contents` and `will-change-transform` utilities to optimize an element that's expected to change in the near future by instructing the browser to prepare the necessary animation before it actually begins:

```html
<!-- [!code classes:will-change-scroll] -->
<div class="overflow-auto will-change-scroll">
  <!-- ... -->
</div>
```

It's recommended that you apply these utilities just before an element changes, and then remove it shortly after it finishes using `will-change-auto`.

The `will-change` property is intended to be used as a last resort when dealing with **known performance problems**. Avoid using these utilities too much, or simply in anticipation of performance issues, as it could actually cause the page to be less performant.

### Using a custom value

<UsingACustomValue
  utility="will-change"
  name={
    <>
      <code>will-change</code> property
    </>
  }
  value="top,left"
  variable="properties"
/>
