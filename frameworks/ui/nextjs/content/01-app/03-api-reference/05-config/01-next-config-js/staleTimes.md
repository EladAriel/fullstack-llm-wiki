---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/staleTimes.mdx"
source_commit: "dcf242a17b5d4622bbd9624db531a9d84177619f"
source_commit_short: "dcf242a1"
source_commit_date: "2026-07-25T10:16:19+02:00"
generated_at: "2026-07-25T11:50:53Z"
---

---
title: staleTimes
description: Learn how to override the invalidation time of the client cache.
version: experimental
---

`staleTimes` is an experimental feature that enables caching of page segments in the [Client Cache](/docs/app/glossary#client-cache).

You can enable this experimental feature and provide custom revalidation times by setting the experimental `staleTimes` flag:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    staleTimes: {
      dynamic: 30,
      static: 180,
    },
  },
}

module.exports = nextConfig
```

The `static` and `dynamic` properties correspond with the time period (in seconds) based on different types of [link prefetching](/docs/app/api-reference/components/link#prefetch).

- The `dynamic` property is used when the page is neither statically generated nor fully prefetched (e.g. with `prefetch={true}`).
  - Default: 0 seconds (not cached)
- The `static` property is used for statically generated pages, or when the `prefetch` prop on `Link` is set to `true`, or when calling [`router.prefetch`](/docs/app/api-reference/functions/use-router).
  - Default: 5 minutes

> **Good to know:**
>
> - [Loading boundaries](/docs/app/api-reference/file-conventions/loading) are considered reusable for the `static` period defined in this configuration.
> - This doesn't affect [partial rendering](/docs/app/getting-started/linking-and-navigating#client-side-transitions), **meaning shared layouts won't automatically be refetched on every navigation, only the page segment that changes.**
> - This doesn't change [back/forward caching](/docs/app/glossary#client-cache) behavior to prevent layout shift and to prevent losing the browser scroll position.

### Version History

| Version   | Changes                                                    |
| --------- | ---------------------------------------------------------- |
| `v15.0.0` | The `dynamic` `staleTimes` default changed from 30s to 0s. |
| `v14.2.0` | Experimental `staleTimes` introduced.                      |
