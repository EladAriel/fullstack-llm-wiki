---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/04-functions/io.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: io
description: API Reference for the io function.
version: draft
---

`io()` informs Next.js that an IO operation will follow this call. When [Cache Components](/docs/app/api-reference/config/next-config-js/cacheComponents) is not enabled or when rendering in Pages Router, signifying IO in this way is not meaningful and the call will always resolve immediately. When Cache Components is enabled, you may be required to add `await io()` preceding synchronous IO that is encountered while prerendering pages (`new Date()` for example). Additionally, if you want to avoid having genuine uncached IO invoked while prerendering, you shield it by preceeding it with `await io()`.

```ts filename="app/page.tsx" switcher
import { io } from 'next/cache'
import { db } from '@/lib/db'

export default async function Page() {
  // Synchronous IO: new Date() would fail during prerender without this
  await io()
  const now = new Date().toISOString()

  // Async IO: the query would run and be discarded during prerender;
  // io() above lets Next.js skip it entirely
  const orders = await db.query('SELECT * FROM orders LIMIT 10')

  return (
    <main>
      <p>Generated at: {now}</p>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>{order.name}</li>
        ))}
      </ul>
    </main>
  )
}
```

```js filename="app/page.js" switcher
import { io } from 'next/cache'
import { db } from '@/lib/db'

export default async function Page() {
  // Synchronous IO: new Date() would fail during prerender without this
  await io()
  const now = new Date().toISOString()

  // Async IO: the query would run and be discarded during prerender;
  // io() above lets Next.js skip it entirely
  const orders = await db.query('SELECT * FROM orders LIMIT 10')

  return (
    <main>
      <p>Generated at: {now}</p>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>{order.name}</li>
        ))}
      </ul>
    </main>
  )
}
```

## How is this different from `connection()`?

[`connection()`](/docs/app/api-reference/functions/connection) requires an active HTTP request context and signals that the component needs request-specific data. It is imported from `next/server`.

`io()` does not require a request context. It can be used inside `"use cache"` scopes, client components, and anywhere you perform IO that should not be included in a static prerender. It is imported from `next/cache`.

Use `connection()` when you need the request itself (cookies, headers, etc.). Use `io()` when you perform IO that is independent of the request but should still prevent static prerendering.

## Reference

### Type

```ts
function io(): Promise<void>
```

### Parameters

- The function does not accept any parameters.

### Returns

- A `Promise<void>` that resolves immediately during a real request or inside a cache scope, and suspends indefinitely during prerendering to prevent static output from including IO-dependent content.

## Good to know

- `io()` is imported from `next/cache`, not `next/server`.
- Inside `"use cache"` scopes, `io()` resolves immediately. The cache captures the IO result at fill time.
- In client components, `io()` resolves immediately since there is no prerender context in the browser.

### Version History

| Version   | Changes     |
| --------- | ----------- |
| `v16.x.x` | `io` added. |
