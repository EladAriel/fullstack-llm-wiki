---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useQueryErrorResetBoundary.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.375375Z"
---
# Usequeryerrorresetboundary

---
id: useQueryErrorResetBoundary
title: useQueryErrorResetBoundary
---

```ts
function useQueryErrorResetBoundary(): QueryErrorResetBoundaryValue;
```

Defined in: [preact-query/src/QueryErrorResetBoundary.tsx:85](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryErrorResetBoundary.tsx#L85)

This hook will reset any query errors within the closest `QueryErrorResetBoundary`. If there is no boundary
defined it will reset them globally.

## Returns

`QueryErrorResetBoundaryValue`

The boundary's QueryErrorResetBoundaryValue.

## Example

```tsx
import { useErrorBoundary } from 'preact/hooks'
import type { ComponentChildren } from 'preact'
import { useQueryErrorResetBoundary } from '@tanstack/preact-query'

function App({ children }: { children: ComponentChildren }) {
  const { reset } = useQueryErrorResetBoundary()
  const [error, resetError] = useErrorBoundary(() => reset())

  if (error) {
    return (
      <div>
        There was an error!
        <button onClick={() => resetError()}>Try again</button>
      </div>
    )
  }

  return children
}
```
