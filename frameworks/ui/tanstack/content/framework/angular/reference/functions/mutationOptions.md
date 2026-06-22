---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/mutationOptions.md"
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

Allows to share and re-use mutation options in a type-safe way.

**Example**

```ts
export class QueriesService {
  private http = inject(HttpClient)
  private queryClient = inject(QueryClient)

  updatePost(id: number) {
    return mutationOptions({
      mutationFn: (post: Post) => Promise.resolve(post),
      mutationKey: ["updatePost", id],
      onSuccess: (newPost) => {
        //           ^? newPost: Post
        this.queryClient.setQueryData(["posts", id], newPost)
      },
    });
  }
}

class ComponentOrService {
  queries = inject(QueriesService)
  id = signal(0)
  mutation = injectMutation(() => this.queries.updatePost(this.id()))

  save() {
    this.mutation.mutate({ title: 'New Title' })
  }
}
```

## Param

The mutation options.

## Call Signature

```ts
function mutationOptions<TData, TError, TVariables, TOnMutateResult>(options): WithRequired<CreateMutationOptions<TData, TError, TVariables, TOnMutateResult>, "mutationKey">;
```

Defined in: [mutation-options.ts:39](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/mutation-options.ts#L39)

Allows to share and re-use mutation options in a type-safe way.

**Example**

```ts
export class QueriesService {
  private http = inject(HttpClient)
  private queryClient = inject(QueryClient)

  updatePost(id: number) {
    return mutationOptions({
      mutationFn: (post: Post) => Promise.resolve(post),
      mutationKey: ["updatePost", id],
      onSuccess: (newPost) => {
        //           ^? newPost: Post
        this.queryClient.setQueryData(["posts", id], newPost)
      },
    });
  }
}

class ComponentOrService {
  queries = inject(QueriesService)
  id = signal(0)
  mutation = injectMutation(() => this.queries.updatePost(this.id()))

  save() {
    this.mutation.mutate({ title: 'New Title' })
  }
}
```

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

`WithRequired`\<[`CreateMutationOptions`](../interfaces/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>, `"mutationKey"`\>

The mutation options.

### Returns

`WithRequired`\<[`CreateMutationOptions`](../interfaces/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>, `"mutationKey"`\>

Mutation options.

## Call Signature

```ts
function mutationOptions<TData, TError, TVariables, TOnMutateResult>(options): Omit<CreateMutationOptions<TData, TError, TVariables, TOnMutateResult>, "mutationKey">;
```

Defined in: [mutation-options.ts:53](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/mutation-options.ts#L53)

Allows to share and re-use mutation options in a type-safe way.

**Example**

```ts
export class QueriesService {
  private http = inject(HttpClient)
  private queryClient = inject(QueryClient)

  updatePost(id: number) {
    return mutationOptions({
      mutationFn: (post: Post) => Promise.resolve(post),
      mutationKey: ["updatePost", id],
      onSuccess: (newPost) => {
        //           ^? newPost: Post
        this.queryClient.setQueryData(["posts", id], newPost)
      },
    });
  }
}

class ComponentOrService {
  queries = inject(QueriesService)
  id = signal(0)
  mutation = injectMutation(() => this.queries.updatePost(this.id()))

  save() {
    this.mutation.mutate({ title: 'New Title' })
  }
}
```

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

`Omit`\<[`CreateMutationOptions`](../interfaces/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>, `"mutationKey"`\>

The mutation options.

### Returns

`Omit`\<[`CreateMutationOptions`](../interfaces/CreateMutationOptions.md)\<`TData`, `TError`, `TVariables`, `TOnMutateResult`\>, `"mutationKey"`\>

Mutation options.
