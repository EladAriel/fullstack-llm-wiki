---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/typescript.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.359569Z"
---
# Typescript

---
id: typescript
title: TypeScript
---

Lit Query is written in TypeScript and reuses TanStack Query Core's type system. The most important rule is the same as every other adapter: give your query and mutation functions well-defined return types, and the result accessors will infer from them.

## Query Inference

```ts
import { LitElement } from 'lit'
import { createQueryController } from '@tanstack/lit-query'

type Todo = {
  id: number
  title: string
}

async function fetchTodos(): Promise<Todo[]> {
  const response = await fetch('/api/todos')
  if (!response.ok) throw new Error('Failed to fetch todos')
  return response.json() as Promise<Todo[]>
}

class TodosView extends LitElement {
  private readonly todos = createQueryController(this, {
    queryKey: ['todos'],
    queryFn: fetchTodos,
  })

  render() {
    const query = this.todos()
    // query.data is Todo[] | undefined until success is known.
  }
}
```

Checking `isSuccess`, `isPending`, `isError`, or `status` narrows the result just like TanStack Query Core result types:

```ts
const query = this.todos()

if (query.isSuccess) {
  query.data
  // Todo[]
}
```

## Mutation Inference

```ts
import { LitElement } from 'lit'
import { createMutationController } from '@tanstack/lit-query'

type CreateTodoInput = {
  title: string
}

type Todo = {
  id: number
  title: string
}

async function addTodo(input: CreateTodoInput): Promise<Todo> {
  const response = await fetch('/api/todos', {
    method: 'POST',
    body: JSON.stringify(input),
  })
  if (!response.ok) throw new Error('Failed to create todo')
  return response.json() as Promise<Todo>
}

class AddTodoButton extends LitElement {
  private readonly mutation = createMutationController(this, {
    mutationFn: addTodo,
  })

  private add() {
    this.mutation.mutate({ title: 'Learn Lit Query' })
  }
}
```

## Extracting Options

Use [`queryOptions`](./reference/functions/queryOptions.md), [`infiniteQueryOptions`](./reference/functions/infiniteQueryOptions.md), and [`mutationOptions`](./reference/functions/mutationOptions.md) when you want to share typed options between controllers and `QueryClient` calls.

```ts
import { LitElement } from 'lit'
import {
  QueryClient,
  createQueryController,
  noop,
  queryOptions,
} from '@tanstack/lit-query'

function todosOptions() {
  return queryOptions({
    queryKey: ['todos'],
    queryFn: fetchTodos,
    staleTime: 5_000,
  })
}

const queryClient = new QueryClient()

class TodosView extends LitElement {
  private readonly todos = createQueryController(this, todosOptions())
}

void queryClient.query(todosOptions()).catch(noop)
```

The branded `queryKey` returned from `queryOptions` also helps APIs like `queryClient.getQueryData` understand the data type.

## Global Register Types

Because `@tanstack/lit-query` re-exports TanStack Query Core, module augmentation is written against `@tanstack/lit-query` in Lit apps:

```ts
import '@tanstack/lit-query'

type AppQueryKey = ['todos' | 'projects', ...ReadonlyArray<unknown>]

declare module '@tanstack/lit-query' {
  interface Register {
    queryKey: AppQueryKey
    mutationKey: AppQueryKey
  }
}
```

See the generated reference for Lit-specific [option and result types](./reference/index.md).
