---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/07-adapters/10-routing-information.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.296307Z"
---
# 10 Routing Information

---
title: Routing Information
description: Reference for routing phases and route fields exposed in `onBuildComplete`.
---

The `routing` object in `onBuildComplete` provides complete routing information with processed patterns ready for deployment:

## `routing.beforeMiddleware`

Routes applied before middleware execution. These include generated header and redirect behavior.

## `routing.middlewareMatchers`

Middleware matcher definitions emitted for this build. Use these to decide whether middleware should be invoked for a given request.

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
