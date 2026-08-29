---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/outputHashSalt.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.304945Z"
---
# Outputhashsalt

---
title: outputHashSalt
description: Learn how to incorporate a custom salt string into content-addressed output filenames.
---

`outputHashSalt` is an option that incorporates a configurable salt string into every content-addressed output filename (chunks, assets). Changing this value forces all output hashes to change, which is useful for invalidating cached assets across deployments without modifying source files.

To configure the output hash salt, set `outputHashSalt` in `next.config.js`:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  outputHashSalt: 'my-deployment-salt',
}

module.exports = nextConfig
```

This works with both Webpack and Turbopack bundlers.

The `NEXT_HASH_SALT` environment variable can also be used for the same purpose. When both are set, the values are **concatenated** (`outputHashSalt + NEXT_HASH_SALT`) to form the effective salt. This lets you combine a per-project salt baked into the config with a per-deployment salt injected at build time via environment variable.

```bash filename="Terminal"
NEXT_HASH_SALT=my-deployment-salt next build
```

## Version History

| Version  | Changes                     |
| -------- | --------------------------- |
| `16.3.0` | `outputHashSalt` was added. |
