---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/middleware.mdx"
source_commit: "dcf242a17b5d4622bbd9624db531a9d84177619f"
source_commit_short: "dcf242a1"
source_commit_date: "2026-07-25T10:16:19+02:00"
generated_at: "2026-07-25T11:50:53Z"
---

---
title: middleware.js
description: API reference for the middleware.js file (deprecated, renamed to proxy.js).
version: draft
related:
  title: Learn more about Proxy
  links:
    - app/api-reference/file-conventions/proxy
---

The `middleware.js` file convention has been **deprecated** in Next.js 16 and renamed to [`proxy.js`](/docs/app/api-reference/file-conventions/proxy).

All functionality remains the same — only the file and export names have changed. See the [Migration to Proxy](/docs/app/api-reference/file-conventions/proxy#migration-to-proxy) section for details on how to migrate.

You can automatically migrate by running:

```bash
npx @next/codemod@canary middleware-to-proxy .
```

For full documentation, see the [`proxy.js` API reference](/docs/app/api-reference/file-conventions/proxy).
