---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/UseSuspenseQueryResult.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: UseSuspenseQueryResult
title: UseSuspenseQueryResult
---

# Type Alias: UseSuspenseQueryResult\<TData, TError\>

```ts
type UseSuspenseQueryResult<TData, TError> = DistributiveOmit<DefinedQueryObserverResult<TData, TError>, "isPlaceholderData" | "promise">;
```

Defined in: [preact-query/src/types.ts:160](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/types.ts#L160)

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`
