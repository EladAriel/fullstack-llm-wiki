---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/window-focus-refetching.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.418866Z"
---
# Window Focus Refetching

---
id: window-focus-refetching
title: Window Focus Refetching
ref: docs/framework/react/guides/window-focus-refetching.md
replace: { '@tanstack/react-query': '@tanstack/angular-query-experimental' }
---

[//]: # 'Example'

```ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideTanStackQuery(
      new QueryClient({
        defaultOptions: {
          queries: {
            refetchOnWindowFocus: false, // default: true
          },
        },
      }),
    ),
  ],
}
```

[//]: # 'Example'
[//]: # 'Example2'

```ts
injectQuery(() => ({
  queryKey: ['todos'],
  queryFn: fetchTodos,
  refetchOnWindowFocus: false,
}))
```

[//]: # 'Example2'
[//]: # 'ReactNative'
[//]: # 'ReactNative'
