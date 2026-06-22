---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/interfaces/HydrationBoundaryProps.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: HydrationBoundaryProps
title: HydrationBoundaryProps
---

# Interface: HydrationBoundaryProps

Defined in: [preact-query/src/HydrationBoundary.tsx:12](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L12)

## Properties

### children?

```ts
optional children: ComponentChildren;
```

Defined in: [preact-query/src/HydrationBoundary.tsx:20](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L20)

***

### options?

```ts
optional options: OmitKeyof<HydrateOptions, "defaultOptions"> & object;
```

Defined in: [preact-query/src/HydrationBoundary.tsx:14](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L14)

#### Type Declaration

##### defaultOptions?

```ts
optional defaultOptions: OmitKeyof<{
}, "mutations">;
```

***

### queryClient?

```ts
optional queryClient: QueryClient;
```

Defined in: [preact-query/src/HydrationBoundary.tsx:21](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L21)

***

### state

```ts
state: DehydratedState | null | undefined;
```

Defined in: [preact-query/src/HydrationBoundary.tsx:13](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L13)
