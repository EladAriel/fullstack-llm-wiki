---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/02-route-segment-config/dynamicParams.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.298265Z"
---
# Dynamicparams

---
title: dynamicParams
description: API reference for the dynamicParams route segment config option.
---

The `dynamicParams` option allows you to control what happens when a dynamic segment is visited that was not generated with [generateStaticParams](/docs/app/api-reference/functions/generate-static-params).

```tsx filename="layout.tsx | page.tsx" switcher
export const dynamicParams = true // true | false
```

```js filename="layout.js | page.js | route.js" switcher
export const dynamicParams = true // true | false
```

- **`true`** (default): Dynamic route segments not included in `generateStaticParams` are generated at request time.
- **`false`**: Dynamic route segments not included in `generateStaticParams` will return a 404.

> **Good to know**:
>
> - This option replaces the `fallback: true | false | blocking` option of `getStaticPaths` in the `pages` directory.
> - `dynamicParams` is not available when [Cache Components](/docs/app/api-reference/config/next-config-js/cacheComponents) is enabled.
