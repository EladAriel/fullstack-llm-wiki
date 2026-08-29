---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-07-dynamic-search.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.958042Z"
---
# 2026 07 Dynamic Search

---
title: July 2026 - Dynamic Search
description: Registries can now handle search server-side.
date: 2026-07-31
---

**Registries can now handle search server-side.**

When you run `shadcn search`, the CLI forwards the search parameters to your
registry as query params:

```txt
GET /r/registry.json?q=button&limit=50&offset=0
```

Return the matching items with a `pagination` object and the CLI uses your
results as-is. This makes search fast for large registries: no more downloading
the full catalog to search it.

```json title="registry.json?q=button&limit=1"
{
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    {
      "name": "button",
      "type": "registry:ui",
      "description": "A button component."
    }
  ],
  "pagination": {
    "total": 12,
    "offset": 0,
    "limit": 1,
    "hasMore": true
  }
}
```

Dynamic search is opt-in. Static registries ignore the query params and keep
working without any changes.

See the [Dynamic Search](/docs/registry/dynamic-search) docs for the full
guide.
