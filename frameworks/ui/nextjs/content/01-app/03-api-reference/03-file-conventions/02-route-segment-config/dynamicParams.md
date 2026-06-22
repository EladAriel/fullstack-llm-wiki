---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/02-route-segment-config/dynamicParams.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

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
