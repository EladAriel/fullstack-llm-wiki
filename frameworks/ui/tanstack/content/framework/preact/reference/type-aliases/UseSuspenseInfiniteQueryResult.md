---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/type-aliases/UseSuspenseInfiniteQueryResult.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: UseSuspenseInfiniteQueryResult
title: UseSuspenseInfiniteQueryResult
---

# Type Alias: UseSuspenseInfiniteQueryResult\<TData, TError\>

```ts
type UseSuspenseInfiniteQueryResult<TData, TError> = OmitKeyof<DefinedInfiniteQueryObserverResult<TData, TError>, "isPlaceholderData" | "promise">;
```

Defined in: [preact-query/src/types.ts:183](https://github.com/theVedanta/query/blob/main/packages/preact-query/src/types.ts#L183)

## Type Parameters

### TData

`TData` = `unknown`

### TError

`TError` = `DefaultError`
