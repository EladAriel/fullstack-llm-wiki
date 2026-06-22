---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/guides/disabling-queries.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

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
