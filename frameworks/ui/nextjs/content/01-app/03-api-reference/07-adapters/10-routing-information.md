---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/07-adapters/10-routing-information.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: Routing Information
description: Reference for routing phases and route fields exposed in `onBuildComplete`.
---

The `routing` object in `onBuildComplete` provides complete routing information with processed patterns ready for deployment:

## `routing.beforeMiddleware`

Routes applied before middleware execution. These include generated header and redirect behavior.

## `routing.beforeFiles`

Rewrite routes checked before filesystem route matching.

## `routing.afterFiles`

Rewrite routes checked after filesystem route matching.

## `routing.dynamicRoutes`

Dynamic matchers generated from route segments such as `[slug]` and catch-all routes.

## `routing.onMatch`

Routes that apply after a successful match, such as immutable cache headers for hashed static assets.

## `routing.fallback`

Final rewrite routes checked when earlier phases did not produce a match.

## Common Route Fields

Each route entry can include:

- `source`: Original route pattern (optional for generated internal rules)
- `sourceRegex`: Compiled regex for matching requests
- `destination`: Internal destination or redirect destination
- `headers`: Headers to apply
- `has`: Positive matching conditions
- `missing`: Negative matching conditions
- `status`: Redirect status code
- `priority`: Internal route priority flag
