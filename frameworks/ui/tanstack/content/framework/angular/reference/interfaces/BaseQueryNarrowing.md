---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/interfaces/BaseQueryNarrowing.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.428905Z"
---
# Basequerynarrowing

---
id: BaseQueryNarrowing
title: BaseQueryNarrowing
---

Defined in: [types.ts:51](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L51)

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`

## Properties

### isError()

```ts
isError: (this) => this is CreateBaseQueryResult<TData, TError, CreateStatusBasedQueryResult<"error", TData, TError>>;
```

Defined in: [types.ts:59](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L59)

#### Parameters

##### this

[`CreateBaseQueryResult`](../type-aliases/CreateBaseQueryResult.md)\<`TData`, `TError`\>

#### Returns

`this is CreateBaseQueryResult<TData, TError, CreateStatusBasedQueryResult<"error", TData, TError>>`

***

### isPending()

```ts
isPending: (this) => this is CreateBaseQueryResult<TData, TError, CreateStatusBasedQueryResult<"pending", TData, TError>>;
```

Defined in: [types.ts:66](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L66)

#### Parameters

##### this

[`CreateBaseQueryResult`](../type-aliases/CreateBaseQueryResult.md)\<`TData`, `TError`\>

#### Returns

`this is CreateBaseQueryResult<TData, TError, CreateStatusBasedQueryResult<"pending", TData, TError>>`

***

### isSuccess()

```ts
isSuccess: (this) => this is CreateBaseQueryResult<TData, TError, CreateStatusBasedQueryResult<"success", TData, TError>>;
```

Defined in: [types.ts:52](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/types.ts#L52)

#### Parameters

##### this

[`CreateBaseQueryResult`](../type-aliases/CreateBaseQueryResult.md)\<`TData`, `TError`\>

#### Returns

`this is CreateBaseQueryResult<TData, TError, CreateStatusBasedQueryResult<"success", TData, TError>>`
