---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/interfaces/HydrationBoundaryProps.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.381931Z"
---
# Hydrationboundaryprops

---
id: HydrationBoundaryProps
title: HydrationBoundaryProps
---

Defined in: [preact-query/src/HydrationBoundary.tsx:17](https://github.com/TanStack/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L17)

The props accepted by `HydrationBoundary`.

## Properties

### children?

```ts
optional children: ComponentChildren;
```

Defined in: [preact-query/src/HydrationBoundary.tsx:37](https://github.com/TanStack/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L37)

The components to render — always rendered unconditionally, not gated on hydration. New queries are
hydrated into the cache during render; for queries that already exist in the cache, only newer dehydrated
data is hydrated, and that happens in an effect after commit, so `children` may render briefly before it
lands.

***

### options?

```ts
optional options: OmitKeyof<HydrateOptions, "defaultOptions"> & object;
```

Defined in: [preact-query/src/HydrationBoundary.tsx:25](https://github.com/TanStack/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L25)

Optional. Note: unlike `hydrate`, `mutations` cannot be set here.

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

Defined in: [preact-query/src/HydrationBoundary.tsx:41](https://github.com/TanStack/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L41)

Use this to use a custom `QueryClient`. Otherwise, the one from the nearest context will be used.

***

### state

```ts
state: DehydratedState | null | undefined;
```

Defined in: [preact-query/src/HydrationBoundary.tsx:21](https://github.com/TanStack/query/blob/main/packages/preact-query/src/HydrationBoundary.tsx#L21)

The state to hydrate.
