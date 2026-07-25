---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/eslint/no-void-query-fn.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
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
