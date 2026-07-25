---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/scroll-behavior.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.069282Z"
---
# Scroll Behavior

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";

export const title = "scroll-behavior";
export const description = "Utilities for controlling the scroll behavior of an element.";

<ApiTable
  rows={[
    ["scroll-auto", "scroll-behavior: auto;"],
    ["scroll-smooth", "scroll-behavior: smooth;"],
  ]}
/>

## Examples

### Using smooth scrolling

Use the `scroll-smooth` utility to enable smooth scrolling within an element:

```html
<!-- [!code classes:scroll-smooth] -->
<html class="scroll-smooth">
  <!-- ... -->
</html>
```

Setting the `scroll-behavior` only affects scroll events that are triggered by the browser.

### Using normal scrolling

Use the `scroll-auto` utility to revert to the default browser behavior for scrolling:

```html
<!-- [!code classes:scroll-auto] -->
<html class="scroll-smooth md:scroll-auto">
  <!-- ... -->
</html>
```
