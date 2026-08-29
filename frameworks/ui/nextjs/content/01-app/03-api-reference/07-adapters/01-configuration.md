---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/07-adapters/01-configuration.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.296007Z"
---
# 01 Configuration

---
title: Configuration
description: Configure `adapterPath` or `NEXT_ADAPTER_PATH` to use a custom deployment adapter.
---

To use an adapter, specify the path to your adapter module in `adapterPath`:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  adapterPath: require.resolve('./my-adapter.js'),
}

module.exports = nextConfig
```

Alternatively `NEXT_ADAPTER_PATH` can be set to enable zero-config usage in deployment platforms.
