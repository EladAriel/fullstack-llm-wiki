---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/solid/guides/suspense.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: suspense
title: Suspense
---

Solid Query can also be used with Solid's [Suspense](https://docs.solidjs.com/reference/components/suspense) API's.

To do that you need to wrap your suspendable component with `Suspense` component provided by Solid

```tsx
import { Suspense } from 'solid-js'
;<Suspense fallback={<LoadingSpinner />}>
  <SuspendableComponent />
</Suspense>
```

You can use async `suspense` function that is provided by `solid-query`.

```tsx
import { useQuery } from '@tanstack/solid-query'

const todoFetcher = async () =>
  await fetch('https://jsonplaceholder.cypress.io/todos').then((response) =>
    response.json(),
  )

function SuspendableComponent() {
  const todosQuery = useQuery(() => ({
    queryKey: ['todos'],
    queryFn: todoFetcher,
  }))

  // Accessing todosQuery.data directly inside a <Suspense> boundary
  // automatically triggers suspension until data is ready
  return <div>Data: {JSON.stringify(todosQuery.data)}</div>
}
```

## Fetch-on-render vs Render-as-you-fetch

Out of the box, Solid Query in `suspense` mode works really well as a **Fetch-on-render** solution with no additional configuration. This means that when your components attempt to mount, they will trigger query fetching and suspend, but only once you have imported them and mounted them. If you want to take it to the next level and implement a **Render-as-you-fetch** model, we recommend implementing [Prefetching](./prefetching) on routing callbacks and/or user interactions events to start loading queries before they are mounted and hopefully even before you start importing or mounting their parent components.
