---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/eslint/no-void-query-fn.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

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
