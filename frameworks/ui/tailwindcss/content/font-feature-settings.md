---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/font-feature-settings.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.745611Z"
---
# Font Feature Settings

import { ApiTable } from "@/components/api-table.tsx";
import { ResponsiveDesign, UsingACustomValue } from "@/components/content.tsx";

export const title = "font-feature-settings";
export const description = "Utilities for controlling advanced typographic features.";

<ApiTable
  rows={[
    ["font-features-[<value>]", "font-feature-settings: <value>;"],
    ["font-features-(<custom-property>)", "font-feature-settings: var(<custom-property>);"],
  ]}
/>

## Examples

### Basic example

Use the `font-features-[<value>]` utility to enable OpenType features in fonts that support them:

```html
<!-- [!code classes:font-features-["smcp"]] -->
<p class="font-features-['smcp'] ...">This text uses small caps.</p>
```

### Enabling multiple features

You can enable multiple OpenType features by separating them with commas:

```html
<!-- [!code classes:font-features-["smcp","onum"]] -->
<p class="font-features-['smcp','onum'] ...">This text uses small caps and oldstyle numbers.</p>
```

### Using CSS variables

Use the `font-features-(<custom-property>)` syntax to apply font feature settings from a CSS variable:

```html
<!-- [!code classes:font-features-(--my-features)] -->
<p class="font-features-(--my-features) ...">
  <!-- ... -->
</p>
```

### Responsive design

<ResponsiveDesign
  property="font-feature-settings"
  defaultClass="font-features-['tnum']"
  featuredClass="font-features-['smcp']"
  element="p"
/>
