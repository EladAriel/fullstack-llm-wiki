---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/quick-start.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.359093Z"
---
# Quick Start

---
id: quick-start
title: Quick Start
---

This snippet shows the three core Lit Query concepts:

- [Queries](./guides/queries.md)
- [Mutations](./guides/mutations.md)
- [Query Invalidation](./guides/query-invalidation.md)

For complete runnable examples, see [Basic](./examples/basic), [Pagination](./examples/pagination), and [SSR](./examples/ssr).

```ts
import { LitElement, html } from 'lit'
import {
  QueryClient,
  QueryClientProvider,
  createMutationController,
  createQueryController,
} from '@tanstack/lit-query'
import { addTodo, getTodos } from './api'

const queryClient = new QueryClient()

class AppQueryProvider extends QueryClientProvider {
  constructor() {
    super()
    this.client = queryClient
  }
}

customElements.define('app-query-provider', AppQueryProvider)

class TodosView extends LitElement {
  private readonly todos = createQueryController(this, {
    queryKey: ['todos'],
    queryFn: getTodos,
  })

  private readonly createTodo = createMutationController(this, {
    mutationFn: addTodo,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['todos'] })
    },
  })

  render() {
    const query = this.todos()
    const mutation = this.createTodo()

    if (query.isPending) return html`Loading...`
    if (query.isError) return html`Error: ${query.error.message}`

    return html`
      <ul>
        ${query.data.map((todo) => html`<li>${todo.title}</li>`)}
      </ul>

      <button
        ?disabled=${mutation.isPending}
        @click=${() => this.createTodo.mutate({ title: 'Write Lit docs' })}
      >
        Add Todo
      </button>
    `
  }
}

customElements.define('todos-view', TodosView)
```

Mount the provider around your component:

```html
<app-query-provider>
  <todos-view></todos-view>
</app-query-provider>
```

The controllers are created with `this` because a `LitElement` is a `ReactiveControllerHost`. Lit Query uses the host lifecycle to subscribe, request updates, and clean up when the element disconnects.

Continue with [Reactive Controllers vs Hooks](./guides/reactive-controllers-vs-hooks.md) if you know React Query, or go straight to [Queries](./guides/queries.md).
