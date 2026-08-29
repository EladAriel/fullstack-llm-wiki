---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/QueryErrorResetBoundary.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.375220Z"
---
# Queryerrorresetboundary

---
id: QueryErrorResetBoundary
title: QueryErrorResetBoundary
---

```ts
function QueryErrorResetBoundary(__namedParameters): Element;
```

Defined in: [preact-query/src/QueryErrorResetBoundary.tsx:159](https://github.com/TanStack/query/blob/main/packages/preact-query/src/QueryErrorResetBoundary.tsx#L159)

When using `suspense` or `throwOnError` in your queries, you need a way to let queries know that you want to
try again when re-rendering after some error occurred. With the `QueryErrorResetBoundary` component you can
reset any query errors within the boundaries of the component.

## Parameters

### \_\_namedParameters

[`QueryErrorResetBoundaryProps`](../interfaces/QueryErrorResetBoundaryProps.md)

## Returns

`Element`

The `children`, rendered as-is, or called with the boundary's QueryErrorResetBoundaryValue
if `children` is a function.

## Example

```tsx
import { useErrorBoundary } from 'preact/hooks'
import type { ComponentChildren } from 'preact'
import { QueryErrorResetBoundary } from '@tanstack/preact-query'

function ErrorBoundary({
  children,
  reset,
}: {
  children: ComponentChildren
  reset: () => void
}) {
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

function App() {
  return (
    <QueryErrorResetBoundary>
      {({ reset }) => (
        <ErrorBoundary reset={reset}>
          <Page />
        </ErrorBoundary>
      )}
    </QueryErrorResetBoundary>
  )
}
```
