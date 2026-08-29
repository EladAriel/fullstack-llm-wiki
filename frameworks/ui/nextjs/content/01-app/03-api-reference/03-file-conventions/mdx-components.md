---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/mdx-components.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.288711Z"
---
# Mdx Components

---
title: mdx-components.js
description: API reference for the mdx-components.js file.
related:
  title: Learn more about MDX Components
  links:
    - app/guides/mdx
---

The `mdx-components.js|tsx` file is **required** to use [`@next/mdx` with App Router](/docs/app/guides/mdx) and will not work without it. Additionally, you can use it to [customize styles](/docs/app/guides/mdx#using-custom-styles-and-components).

Use the file `mdx-components.tsx` (or `.js`) in the root of your project to define MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.

```tsx filename="mdx-components.tsx" switcher
import type { MDXComponents } from 'mdx/types'

const components: MDXComponents = {}

export function useMDXComponents(): MDXComponents {
  return components
}
```

```js filename="mdx-components.js" switcher
const components = {}

export function useMDXComponents() {
  return components
}
```

## Exports

### `useMDXComponents` function

The file must export a single function named `useMDXComponents`. This function does not accept any arguments.

```tsx filename="mdx-components.tsx" switcher
import type { MDXComponents } from 'mdx/types'

const components: MDXComponents = {}

export function useMDXComponents(): MDXComponents {
  return components
}
```

```js filename="mdx-components.js" switcher
const components = {}

export function useMDXComponents() {
  return components
}
```

## Version History

| Version   | Changes              |
| --------- | -------------------- |
| `v13.1.2` | MDX Components added |
