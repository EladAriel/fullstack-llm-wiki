---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/02-route-segment-config/dynamicParams.mdx"
source_commit: "dcf242a17b5d4622bbd9624db531a9d84177619f"
source_commit_short: "dcf242a1"
source_commit_date: "2026-07-25T10:16:19+02:00"
generated_at: "2026-07-25T11:50:53Z"
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
