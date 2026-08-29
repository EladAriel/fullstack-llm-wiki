---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/turbopackFileSystemCache.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.306040Z"
---
# Turbopackfilesystemcache

---
title: Turbopack FileSystem Caching
nav_title: turbopackFileSystemCache
description: Learn how to enable and configure FileSystem Caching for Turbopack builds
---

## Usage

Turbopack FileSystem Cache enables Turbopack to reduce work across `next dev` or `next build` commands. When enabled, Turbopack will save and restore data under the `.next` directory between runs, which can greatly speed up subsequent builds and dev sessions.

Two options control the cache, one for `next dev` and one for `next build`. Both are enabled by default:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    turbopackFileSystemCacheForDev: true,
    turbopackFileSystemCacheForBuild: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    turbopackFileSystemCacheForDev: true,
    turbopackFileSystemCacheForBuild: true,
  },
}

module.exports = nextConfig
```

## Options

- **`turbopackFileSystemCacheForDev`** (default: `true`): caches Turbopack's work for `next dev` in `.next/dev/cache/turbopack`. Restarting the dev server reuses the previous compilation.
- **`turbopackFileSystemCacheForBuild`** (default: `true`): caches Turbopack's work for `next build` in `.next/cache/turbopack`. Subsequent builds start warm. See [Build environments](#build-environments).

Set either option to `false` to opt out.

## Build environments

The build cache lives in `.next/cache`. Builds only get faster when that directory is restored before each build.

- **Self-hosted builds**: reuse the same working directory between builds. Containerized builds start from a clean layer and do not carry `.next/cache` over unless you cache or mount it explicitly.
- **CI providers**: [configure build caching](/docs/app/guides/ci-build-caching) for `.next/cache`.

If your build environment never preserves `.next/cache`, set `turbopackFileSystemCacheForBuild: false` to skip writing a cache that will not be read.

## Version History

| Version   | Changes                                                        |
| --------- | -------------------------------------------------------------- |
| `v16.3.0` | FileSystem caching is enabled by default for builds            |
| `v16.1.0` | FileSystem caching is enabled by default for development       |
| `v16.0.0` | Beta release with separate flags for build and dev             |
| `v15.5.0` | Persistent caching released as experimental on canary releases |
