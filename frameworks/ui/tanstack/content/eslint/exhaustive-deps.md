---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/eslint/exhaustive-deps.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.354634Z"
---
# Exhaustive Deps

---
id: exhaustive-deps
title: Exhaustive dependencies for query keys
---

Query keys should contain the serializable values that identify the data returned by your queryFn.
This makes sure that queries are cached independently and that queries are refetched automatically when those values change.

Function call targets are not query key dependencies. For example, `fetchTodoById(todoId)` needs `todoId` in the query key, but not `fetchTodoById`. Values referenced inside nested callbacks are still dependencies, so `promise.then(() => todoId)` also needs `todoId` in the query key.

## Rule Details

Examples of **incorrect** code for this rule:

```tsx
/* eslint "@tanstack/query/exhaustive-deps": "error" */

useQuery({
  queryKey: ['todo'],
  queryFn: () => api.getTodo(todoId),
})

const todoQueries = {
  detail: (id) => ({ queryKey: ['todo'], queryFn: () => api.getTodo(id) }),
}
```

Examples of **correct** code for this rule:

```tsx
const Component = ({ todoId }) => {
  const todos = useTodos()
  useQuery({
    queryKey: ['todo', todoId],
    queryFn: () => todos.getTodo(todoId),
  })
}
```

```tsx
const todos = createTodos()
const todoQueries = {
  detail: (id) => ({
    queryKey: ['todo', id],
    queryFn: () => todos.getTodo(id),
  }),
}
```

```tsx
// with { allowlist: { types: ["Config"] }}
class Config { ... }
const Component = ({ todoId, config }: { todoId: string, config: Config }) => {
  useQuery({
    queryKey: ['todo', todoId],
    queryFn: () => fetchTodo(todoId, config.baseUrl),
  })
}
```

### Options

- `allowlist.variables`: An array of variable names that should be ignored when checking dependencies
- `allowlist.types`: An array of TypeScript type names that should be ignored when checking dependencies

```json
{
  "@tanstack/query/exhaustive-deps": [
    "error",
    {
      "allowlist": {
        "variables": ["api", "config"],
        "types": ["ApiClient", "Config"]
      }
    }
  ]
}
```

## When Not To Use It

If you don't care about the rules of the query keys, then you will not need this rule.

## Attributes

- [x] ✅ Recommended
- [x] 🔧 Fixable
