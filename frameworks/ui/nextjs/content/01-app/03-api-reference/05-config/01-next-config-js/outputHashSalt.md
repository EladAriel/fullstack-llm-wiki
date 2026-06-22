---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/outputHashSalt.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: outputHashSalt
description: Learn how to incorporate a custom salt string into content-addressed output filenames.
version: experimental
---

`outputHashSalt` is an experimental option that incorporates a configurable salt string into every content-addressed output filename (chunks, assets). Changing this value forces all output hashes to change, which is useful for invalidating cached assets across deployments without modifying source files.

To configure the output hash salt, set `experimental.outputHashSalt` in `next.config.js`:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    outputHashSalt: 'my-deployment-salt',
  },
}

module.exports = nextConfig
```

This works with both Webpack and Turbopack bundlers.

The `NEXT_HASH_SALT` environment variable can also be used for the same purpose. When both are set, the values are **concatenated** (`experimental.outputHashSalt + NEXT_HASH_SALT`) to form the effective salt. This lets you combine a per-project salt baked into the config with a per-deployment salt injected at build time via environment variable.

```bash filename="Terminal"
NEXT_HASH_SALT=my-deployment-salt next build
```

## Version History

| Version  | Changes                                  |
| -------- | ---------------------------------------- |
| `16.3.0` | `experimental.outputHashSalt` was added. |
