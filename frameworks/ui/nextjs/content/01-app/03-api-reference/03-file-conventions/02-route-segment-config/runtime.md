---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/02-route-segment-config/runtime.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: runtime
description: API reference for the runtime route segment config option.
---

The `runtime` option allows you to select the JavaScript runtime used for rendering your route.

```tsx filename="layout.tsx | page.tsx | route.ts" switcher
export const runtime = 'nodejs'
// 'nodejs'
```

```js filename="layout.js | page.js | route.js" switcher
export const runtime = 'nodejs'
// 'nodejs'
```

- **`'nodejs'`** (default)
- **`'edge'`** (deprecated)

> **Good to know**:
>
> - The Edge Runtime is deprecated. Remove the `runtime` export from your route files. See [Edge Runtime Deprecated](/docs/messages/edge-runtime-deprecated).
> - This option cannot be used in [Proxy](/docs/app/api-reference/file-conventions/proxy).
