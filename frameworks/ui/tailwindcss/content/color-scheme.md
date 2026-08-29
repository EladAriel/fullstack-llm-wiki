---
type: "Framework Learn Page"
framework: "Tailwind CSS"
source_repo: "https://github.com/tailwindlabs/tailwindcss.com.git"
source_branch: "main"
source_path: "src/docs/color-scheme.mdx"
source_commit: "bd868a314bd05ca78acd047e3da289274dd6ccd7"
source_commit_short: "bd868a3"
source_commit_date: "2026-08-11T20:09:16+02:00"
generated_at: "2026-08-29T09:40:31.752121Z"
---
# Color Scheme

import { ApiTable } from "@/components/api-table.tsx";
import { Example } from "@/components/example.tsx";
import { Figure } from "@/components/figure.tsx";
import { TargetingSpecificStates } from "@/components/content.tsx";

export const title = "color-scheme";
export const description = "Utilities for controlling the color scheme of an element.";

<ApiTable
  rows={[
    ["scheme-normal", "color-scheme: normal;"],
    ["scheme-dark", "color-scheme: dark;"],
    ["scheme-light", "color-scheme: light;"],
    ["scheme-light-dark", "color-scheme: light dark;"],
    ["scheme-only-dark", "color-scheme: only dark;"],
    ["scheme-only-light", "color-scheme: only light;"],
  ]}
/>

## Examples

### Basic example

Use utilities like `scheme-light` and `scheme-light-dark` to control how element should be rendered:

<Figure hint="Try switching your system color scheme to see the difference">

<Example>
  {
    <div className="flex justify-between gap-8 text-sm max-sm:flex-col">
      <div className="flex grow flex-col items-center gap-3 text-center scheme-light">
        <p className="font-mono font-medium text-gray-500 dark:text-gray-400">scheme-light</p>
        <input
          type="date"
          className="w-full rounded-lg border border-gray-950/10 bg-[Field] px-3 py-2 text-[FieldText] dark:border-white/10"
        />
      </div>
      <div className="flex grow flex-col items-center gap-3 text-center scheme-dark">
        <p className="font-mono font-medium text-gray-500 dark:text-gray-400">scheme-dark</p>
        <input
          type="date"
          className="w-full rounded-lg border border-gray-950/10 bg-[Field] px-3 py-2 text-[FieldText] dark:border-white/10"
        />
      </div>
      <div className="flex grow flex-col items-center gap-3 text-center scheme-light-dark">
        <p className="font-medium text-gray-500 dark:text-gray-400">scheme-light-dark</p>
        <input
          type="date"
          className="w-full rounded-lg border border-gray-950/10 bg-[Field] px-3 py-2 text-[FieldText] dark:border-white/10"
        />
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:scheme-light-dark,scheme-light,scheme-dark] -->
<div class="scheme-light ...">
  <input type="date" />
</div>

<div class="scheme-dark ...">
  <input type="date" />
</div>

<div class="scheme-light-dark ...">
  <input type="date" />
</div>
```

</Figure>

### Applying in dark mode

<TargetingSpecificStates
  element="html"
  property="color-scheme"
  variant="dark"
  defaultClass="scheme-light"
  featuredClass="scheme-dark"
/>
