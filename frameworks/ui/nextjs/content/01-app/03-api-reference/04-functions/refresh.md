---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/04-functions/refresh.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.279835Z"
---
# Refresh

---
title: refresh
description: API Reference for the refresh function.
related:
  links:
    - app/guides/server-actions
---

`refresh` allows you to refresh the client router from within a [Server Action](/docs/app/guides/server-actions).

## Usage

`refresh` can **only** be called from within Server Actions. It cannot be used in Route Handlers, Client Components, or any other context.

## Parameters

```tsx
refresh(): void;
```

## Returns

`refresh` does not return a value.

## Examples

```ts filename="app/actions.ts" switcher
'use server'

import { refresh } from 'next/cache'

export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })

  refresh()
}
```

```js filename="app/actions.js" switcher
'use server'

import { refresh } from 'next/cache'

export async function createPost(formData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })

  refresh()
}
```

### Error when used outside Server Actions

```ts filename="app/api/posts/route.ts" switcher
import { refresh } from 'next/cache'

export async function POST() {
  // This will throw an error
  refresh()
}
```
