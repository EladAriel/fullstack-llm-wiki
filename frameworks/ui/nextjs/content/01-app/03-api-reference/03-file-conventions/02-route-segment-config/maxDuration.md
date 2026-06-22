---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/02-route-segment-config/maxDuration.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: maxDuration
description: API reference for the maxDuration route segment config option.
---

The `maxDuration` option allows you to set the maximum execution time (in seconds) for server-side logic in a route segment. Deployment platforms can use `maxDuration` from the Next.js build output to add specific execution limits.

```tsx filename="layout.tsx | page.tsx | route.ts" switcher
export const maxDuration = 5
```

```js filename="layout.js | page.js | route.js" switcher
export const maxDuration = 5
```

## Server Actions

If using [Server Actions](/docs/app/getting-started/mutating-data), set the `maxDuration` at the page level to change the default timeout of all Server Actions used on the page.

## Version History

| Version    | Changes                   |
| ---------- | ------------------------- |
| `v13.4.10` | `maxDuration` introduced. |
