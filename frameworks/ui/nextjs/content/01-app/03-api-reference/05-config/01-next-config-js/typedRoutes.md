---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/typedRoutes.mdx"
source_commit: "dcf242a17b5d4622bbd9624db531a9d84177619f"
source_commit_short: "dcf242a1"
source_commit_date: "2026-07-25T10:16:19+02:00"
generated_at: "2026-07-25T11:50:53Z"
---

---
title: typedRoutes
description: Enable support for statically typed links.
---

> **Note**: This option has been marked as stable, so you should use `typedRoutes` instead of `experimental.typedRoutes`.

Support for [statically typed links](/docs/app/api-reference/config/typescript#statically-typed-links). This feature requires using TypeScript in your project.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  typedRoutes: true,
}

module.exports = nextConfig
```
