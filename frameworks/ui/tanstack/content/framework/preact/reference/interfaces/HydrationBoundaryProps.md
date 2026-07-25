---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/interfaces/HydrationBoundaryProps.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
