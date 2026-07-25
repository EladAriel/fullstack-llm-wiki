---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/color.mdx"
source_commit: "1e700c43f5f270a1a55c4a33e71f01952f24b8c2"
source_commit_short: "1e700c4"
source_commit_date: "2026-07-16T19:14:03+02:00"
generated_at: "2026-07-25T13:40:03.116190Z"
---
# Color

import { ApiTable } from "@/components/api-table.tsx";
import {
  CustomizingYourThemeColors,
  ResponsiveDesign,
  TargetingSpecificStates,
  UsingACustomValue,
} from "@/components/content.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import colors from "./utils/colors";

export const title = "color";
export const description = "Utilities for controlling the text color of an element.";

<ApiTable
  rows={[
    ["text-inherit", "color: inherit;"],
    ["text-current", "color: currentColor;"],
    ["text-transparent", "color: transparent;"],
    ...Object.entries(colors).map(([name, value]) => [`text-${name}`, `color: var(--color-${name}); /* ${value} */`]),
    ["text-(<custom-property>)", "color: var(<custom-property>);"],
    ["text-[<value>]", "color: <value>;"],
  ]}
/>

## Examples

### Basic example

Use utilities like `text-blue-600` and `text-sky-400` to control the text color of an element:

<Figure>

<Example>
  {
    <div className="relative text-center text-xl leading-6 font-medium">
      <p className="text-blue-600 dark:text-sky-400">The quick brown fox jumps over the lazy dog.</p>
    </div>
  }
</Example>

```html
<!-- [!code classes:text-blue-600,dark:text-sky-400] -->
<p class="text-blue-600 dark:text-sky-400">The quick brown fox...</p>
```

</Figure>

### Changing the opacity

Use the color opacity modifier to control the text color opacity of an element:

<Figure>

<Example>
  {
    <div className="space-y-4 text-center text-xl leading-6 font-medium">
      <p className="text-blue-600/100 dark:text-sky-400/100">The quick brown fox jumps over the lazy dog.</p>
      <p className="text-blue-600/75 dark:text-sky-400/75">The quick brown fox jumps over the lazy dog.</p>
      <p className="text-blue-600/50 dark:text-sky-400/50">The quick brown fox jumps over the lazy dog.</p>
      <p className="text-blue-600/25 dark:text-sky-400/25">The quick brown fox jumps over the lazy dog.</p>
    </div>
  }
</Example>

```html
<!-- [!code word:\/100] -->
<!-- [!code word:\/75] -->
<!-- [!code word:\/50] -->
<!-- [!code word:\/25] -->
<p class="text-blue-600/100 dark:text-sky-400/100">The quick brown fox...</p>
<p class="text-blue-600/75 dark:text-sky-400/75">The quick brown fox...</p>
<p class="text-blue-600/50 dark:text-sky-400/50">The quick brown fox...</p>
<p class="text-blue-600/25 dark:text-sky-400/25">The quick brown fox...</p>
```

</Figure>

### Using a custom value

<UsingACustomValue element="p" utility="text" name="text color" variable="color" value="#50d71e" />

### Applying on hover

<TargetingSpecificStates property="color">

<Figure hint="Hover over the text to see the expected behavior">

<Example>
  {
    <p className="text-center text-xl font-medium text-gray-900 dark:text-gray-200">
      Oh I gotta get on that{" "}
      <a
        href="https://en.wikipedia.org/wiki/Internet"
        target="_blank"
        className="underline hover:text-blue-600 dark:hover:text-blue-400"
      >
        internet
      </a>
      , I'm late on everything!
    </p>
  }
</Example>

```html
<!-- [!code classes:hover:text-blue-600,dark:hover:text-blue-400] -->
<!-- prettier-ignore -->
<p class="...">
  Oh I gotta get on that
  <a class="underline hover:text-blue-600 dark:hover:text-blue-400" href="https://en.wikipedia.org/wiki/Internet">internet</a>,
  I'm late on everything!
</p>
```

</Figure>

</TargetingSpecificStates>

### Responsive design

<ResponsiveDesign element="p" property="color" defaultClass="text-blue-600" featuredClass="text-green-600" />

## Customizing your theme

<CustomizingYourThemeColors element="p" utility="text" />
