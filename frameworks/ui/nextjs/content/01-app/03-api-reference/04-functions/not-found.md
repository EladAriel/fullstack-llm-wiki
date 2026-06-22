---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/04-functions/not-found.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: notFound
description: API Reference for the notFound function.
---

The `notFound` function allows you to render the [`not-found file`](/docs/app/api-reference/file-conventions/not-found) within a route segment as well as inject a [`<meta name="robots" content="noindex" />`](/docs/app/api-reference/file-conventions/loading#status-codes) tag for search engines.

## `notFound()`

Invoking the `notFound()` function throws a `NEXT_HTTP_ERROR_FALLBACK;404` error and terminates rendering of the route segment in which it was thrown. Specifying a [**not-found** file](/docs/app/api-reference/file-conventions/not-found) allows you to gracefully handle such errors by rendering a Not Found UI within the segment.

```jsx filename="app/user/[id]/page.js"
import { notFound } from 'next/navigation'

async function fetchUser(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}

export default async function Profile({ params }) {
  const { id } = await params
  const user = await fetchUser(id)

  if (!user) {
    notFound()
  }

  // ...
}
```

> **Good to know**: `notFound()` does not require you to use `return notFound()` due to using the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.

## Version History

| Version   | Changes                |
| --------- | ---------------------- |
| `v13.0.0` | `notFound` introduced. |
