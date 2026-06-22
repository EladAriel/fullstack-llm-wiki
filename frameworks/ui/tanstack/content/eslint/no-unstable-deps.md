---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/eslint/no-unstable-deps.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: no-unstable-deps
title: Disallow putting the result of query hooks directly in a React hook dependency array
---

The object returned from the following query hooks is **not** referentially stable:

- `useQuery`
- `useSuspenseQuery`
- `useQueries`
- `useSuspenseQueries`
- `useInfiniteQuery`
- `useSuspenseInfiniteQuery`
- `useMutation`

The object returned from those hooks should **not** be put directly into the dependency array of a React hook (e.g. `useEffect`, `useMemo`, `useCallback`).
Instead, destructure the return value of the query hook and pass the destructured values into the dependency array of the React hook.

## Rule Details

Examples of **incorrect** code for this rule:

```tsx
/* eslint "@tanstack/query/no-unstable-deps": "warn" */
import { useCallback } from 'react'
import { useMutation } from '@tanstack/react-query'

function Component() {
  const mutation = useMutation({ mutationFn: (value: string) => value })
  const callback = useCallback(() => {
    mutation.mutate('hello')
  }, [mutation])
  return null
}
```

Examples of **correct** code for this rule:

```tsx
/* eslint "@tanstack/query/no-unstable-deps": "warn" */
import { useCallback } from 'react'
import { useMutation } from '@tanstack/react-query'

function Component() {
  const { mutate } = useMutation({ mutationFn: (value: string) => value })
  const callback = useCallback(() => {
    mutate('hello')
  }, [mutate])
  return null
}
```

## Attributes

- [x] ✅ Recommended
- [ ] 🔧 Fixable
