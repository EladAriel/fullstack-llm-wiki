---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/07-adapters/10-routing-information.mdx"
source_commit: "dcf242a17b5d4622bbd9624db531a9d84177619f"
source_commit_short: "dcf242a1"
source_commit_date: "2026-07-25T10:16:19+02:00"
generated_at: "2026-07-25T11:50:53Z"
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
