---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/guides/disabling-queries.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.367802Z"
---
# Disabling Queries

---
id: disabling-queries
title: Disabling/Pausing Queries
ref: docs/framework/react/guides/disabling-queries.md
replace: { 'react-query': 'preact-query', 'React': 'Preact' }
---

[//]: # 'Example2'

```tsx
function Todos() {
  const [filter, setFilter] = useState('')

  const { data } = useQuery({
    queryKey: ['todos', filter],
    queryFn: () => fetchTodos(filter),
    // ⬇️ disabled as long as the filter is empty
    enabled: !!filter,
  })

  return (
    <div>
      // 🚀 applying the filter will enable and execute the query
      <FiltersForm onApply={setFilter} />
      {data && <TodosTable data={data} />}
    </div>
  )
}
```

[//]: # 'Example2'
[//]: # 'Example3'

```tsx
import { skipToken, useQuery } from '@tanstack/preact-query'

function Todos() {
  const [filter, setFilter] = useState<string | undefined>()

  const { data } = useQuery({
    queryKey: ['todos', filter],
    // ⬇️ disabled as long as the filter is undefined or empty
    queryFn: filter ? () => fetchTodos(filter) : skipToken,
  })

  return (
    <div>
      // 🚀 applying the filter will enable and execute the query
      <FiltersForm onApply={setFilter} />
      {data && <TodosTable data={data} />}
    </div>
  )
}
```

[//]: # 'Example3'
