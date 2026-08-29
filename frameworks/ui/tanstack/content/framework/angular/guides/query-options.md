---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/query-options.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.418425Z"
---
# Query Options

---
id: query-options
title: Query Options
ref: docs/framework/react/guides/query-options.md
---

[//]: # 'Example1'

```ts
import { queryOptions, noop } from '@tanstack/angular-query-experimental'

@Injectable({
  providedIn: 'root',
})
export class QueriesService {
  private http = inject(HttpClient)

  post(postId: number) {
    return queryOptions({
      queryKey: ['post', postId],
      queryFn: () => {
        return lastValueFrom(
          this.http.get<Post>(
            `https://jsonplaceholder.typicode.com/posts/${postId}`,
          ),
        )
      },
    })
  }
}

// usage:

postId = input.required({
  transform: numberAttribute,
})
queries = inject(QueriesService)

postQuery = injectQuery(() => this.queries.post(this.postId()))

queryClient.query(this.queries.post(23)).catch(noop)
queryClient.setQueryData(this.queries.post(42).queryKey, newPost)
```

[//]: # 'Example1'
[//]: # 'Example2'

```ts
// Type inference still works, so query.data will be the return type of select instead of queryFn
queries = inject(QueriesService)

query = injectQuery(() => ({
  ...groupOptions(1),
  select: (data) => data.title,
}))
```

[//]: # 'Example2'
