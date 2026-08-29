---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/QueriesResultAccessor.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.391218Z"
---
# Queriesresultaccessor

---
id: QueriesResultAccessor
title: QueriesResultAccessor
---

```ts
type QueriesResultAccessor<TCombinedResult> = ValueAccessor<TCombinedResult> & object;
```

Defined in: [packages/lit-query/src/createQueriesController.ts:218](https://github.com/TanStack/query/blob/main/packages/lit-query/src/createQueriesController.ts#L218)

Accessor returned by `createQueriesController`.

Call the accessor or read its `current` property to get the latest combined
value.

## Type Declaration

### destroy()

```ts
destroy: () => void;
```

Removes the controller from its Lit host and unsubscribes observers.

#### Returns

`void`

## Type Parameters

### TCombinedResult

`TCombinedResult`
