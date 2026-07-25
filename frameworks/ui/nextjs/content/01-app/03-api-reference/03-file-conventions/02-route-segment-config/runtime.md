---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/02-route-segment-config/runtime.mdx"
source_commit: "dcf242a17b5d4622bbd9624db531a9d84177619f"
source_commit_short: "dcf242a1"
source_commit_date: "2026-07-25T10:16:19+02:00"
generated_at: "2026-07-25T11:50:53Z"
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
