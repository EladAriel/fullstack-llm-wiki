---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/svelte/reference/functions/mutationOptions.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: mutationOptions
title: mutationOptions
---

# Function: mutationOptions()

## Call Signature

```ts
function mutationOptions<TData, TError, TVariables, TOnMutateResult>(options): WithRequired<CreateMutationOptions<TData, TError, TVariables, TOnMutateResult>, 'mutationKey'>
```

Defined in: [packages/svelte-query/src/mutationOptions.ts](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/mutationOptions.ts)

### Type Parameters

#### TData

`TData` = `unknown`

#### TError

`TError` = `Error`

#### TVariables

`TVariables` = `void`

#### TOnMutateResult

`TOnMutateResult` = `unknown`

### Parameters

#### options

`WithRequired`\<[`CreateMutationOptions`](../type-aliases/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>, `'mutationKey'`\>

### Returns

`WithRequired`\<[`CreateMutationOptions`](../type-aliases/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>, `'mutationKey'`\>

## Call Signature

```ts
function mutationOptions<TData, TError, TVariables, TOnMutateResult>(options): Omit<CreateMutationOptions<TData, TError, TVariables, TOnMutateResult>, 'mutationKey'>
```

Defined in: [packages/svelte-query/src/mutationOptions.ts](https://github.com/TanStack/query/blob/main/packages/svelte-query/src/mutationOptions.ts)

### Type Parameters

#### TData

`TData` = `unknown`

#### TError

`TError` = `Error`

#### TVariables

`TVariables` = `void`

#### TOnMutateResult

`TOnMutateResult` = `unknown`

### Parameters

#### options

`Omit`\<[`CreateMutationOptions`](../type-aliases/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>, `'mutationKey'`\>

### Returns

`Omit`\<[`CreateMutationOptions`](../type-aliases/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>, `'mutationKey'`\>
