---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/eslint/no-void-query-fn.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.355911Z"
---
# No Void Query Fn

---
id: no-void-query-fn
title: Disallow returning void from query functions
---

Query functions must return a value that will be cached by TanStack Query. Functions that don't return a value (void functions) can lead to unexpected behavior and might indicate a mistake in the implementation.

## Rule Details

Example of **incorrect** code for this rule:

```tsx
/* eslint "@tanstack/query/no-void-query-fn": "error" */

useQuery({
  queryKey: ['todos'],
  queryFn: async () => {
    await api.todos.fetch() // Function doesn't return the fetched data
  },
})
```

Example of **correct** code for this rule:

```tsx
/* eslint "@tanstack/query/no-void-query-fn": "error" */
useQuery({
  queryKey: ['todos'],
  queryFn: async () => {
    const todos = await api.todos.fetch()
    return todos
  },
})
```

## Attributes

- [x] ✅ Recommended
- [ ] 🔧 Fixable
