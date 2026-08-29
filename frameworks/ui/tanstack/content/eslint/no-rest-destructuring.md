---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/eslint/no-rest-destructuring.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.355756Z"
---
# No Rest Destructuring

---
id: no-rest-destructuring
title: Disallow object rest destructuring on query results
---

Use object rest destructuring on query results automatically subscribes to every field of the query result, which may cause unnecessary re-renders.
This makes sure that you only subscribe to the fields that you actually need.

## Rule Details

Examples of **incorrect** code for this rule:

```tsx
/* eslint "@tanstack/query/no-rest-destructuring": "warn" */

const useTodos = () => {
  const { data: todos, ...rest } = useQuery({
    queryKey: ['todos'],
    queryFn: () => api.getTodos(),
  })
  return { todos, ...rest }
}
```

Examples of **correct** code for this rule:

```tsx
const todosQuery = useQuery({
  queryKey: ['todos'],
  queryFn: () => api.getTodos(),
})

// normal object destructuring is fine
const { data: todos } = todosQuery
```

When [typed linting](https://typescript-eslint.io/getting-started/typed-linting/) is enabled, the rule also flags rest destructuring on custom hooks that return a TanStack Query result.

## When Not To Use It

If you set the `notifyOnChangeProps` options manually, you can disable this rule.
Since you are not using tracked queries, you are responsible for specifying which props should trigger a re-render.

## Attributes

- [x] ✅ Recommended
- [ ] 🔧 Fixable
