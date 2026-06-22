---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/staticGeneration.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: staticGeneration*
description: Learn how to configure static generation in your Next.js application.
version: experimental
---

The `staticGeneration*` options allow you to configure the Static Generation process for advanced use cases.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    staticGenerationRetryCount: 1,
    staticGenerationMaxConcurrency: 8,
    staticGenerationMinPagesPerWorker: 25,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
const nextConfig = {
  experimental: {
    staticGenerationRetryCount: 1,
    staticGenerationMaxConcurrency: 8,
    staticGenerationMinPagesPerWorker: 25,
  },
}

export default nextConfig
```

## Config Options

The following options are available:

- `staticGenerationRetryCount`: The number of times to retry a failed page generation before failing the build.
- `staticGenerationMaxConcurrency`: The maximum number of pages to be processed per worker.
- `staticGenerationMinPagesPerWorker`: The minimum number of pages to be processed before starting a new worker.
