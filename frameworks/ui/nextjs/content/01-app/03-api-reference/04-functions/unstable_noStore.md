---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/04-functions/unstable_noStore.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: unstable_noStore
description: API Reference for the unstable_noStore function.
version: legacy
---

**In version 15, we recommend using [`connection`](/docs/app/api-reference/functions/connection) instead of `unstable_noStore`.**

`unstable_noStore` can be used to declaratively opt out of prerendering and indicate a particular component should not be cached.

```jsx
import { unstable_noStore as noStore } from 'next/cache';

export default async function ServerComponent() {
  noStore();
  const result = await db.query(...);
  ...
}
```

> **Good to know**:
>
> - `unstable_noStore` is equivalent to `cache: 'no-store'` on a `fetch`
> - `unstable_noStore` is preferred over `export const dynamic = 'force-dynamic'` as it is more granular and can be used on a per-component basis

- Using `unstable_noStore` inside [`unstable_cache`](/docs/app/api-reference/functions/unstable_cache) will not opt out of static generation. Instead, it will defer to the cache configuration to determine whether to cache the result or not.

## Usage

If you prefer not to pass additional options to `fetch`, like `cache: 'no-store'`, `next: { revalidate: 0 }` or in cases where `fetch` is not available, you can use `noStore()` as a replacement for all of these use cases.

```jsx
import { unstable_noStore as noStore } from 'next/cache';

export default async function ServerComponent() {
  noStore();
  const result = await db.query(...);
  ...
}
```

## Version History

| Version   | Changes                                         |
| --------- | ----------------------------------------------- |
| `v15.0.0` | `unstable_noStore` deprecated for `connection`. |
| `v14.0.0` | `unstable_noStore` introduced.                  |
