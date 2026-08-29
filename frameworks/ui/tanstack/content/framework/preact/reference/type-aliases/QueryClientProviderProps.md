---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/QueryClientProviderProps.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.380972Z"
---
# Queryclientproviderprops

---
id: QueryClientProviderProps
title: QueryClientProviderProps
---

```ts
type QueryClientProviderProps = object;
```

Defined in: [preact-query/src/QueryClientProvider.tsx:38](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryClientProvider.tsx#L38)

The props accepted by `QueryClientProvider`.

## Properties

### children?

```ts
optional children: ComponentChildren;
```

Defined in: [preact-query/src/QueryClientProvider.tsx:48](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryClientProvider.tsx#L48)

The components that get access to the provided `QueryClient`.

***

### client

```ts
client: QueryClient;
```

Defined in: [preact-query/src/QueryClientProvider.tsx:44](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryClientProvider.tsx#L44)

**Required**

The `QueryClient` instance to provide.
