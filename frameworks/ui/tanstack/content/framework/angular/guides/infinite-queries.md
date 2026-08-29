---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/guides/infinite-queries.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.416992Z"
---
# Infinite Queries

---
id: infinite-queries
title: Infinite Queries
ref: docs/framework/react/guides/infinite-queries.md
replace:
  { 'useQuery': 'injectQuery', 'useInfiniteQuery': 'injectInfiniteQuery' }
---

[//]: # 'Example'

```angular-ts
import { Component, computed, inject } from '@angular/core'
import { injectInfiniteQuery } from '@tanstack/angular-query-experimental'
import { lastValueFrom } from 'rxjs'
import { ProjectsService } from './projects-service'

@Component({
  selector: 'example',
  templateUrl: './example.component.html',
})
export class Example {
  projectsService = inject(ProjectsService)

  query = injectInfiniteQuery(() => ({
    queryKey: ['projects'],
    queryFn: async ({ pageParam }) => {
      return lastValueFrom(this.projectsService.getProjects(pageParam))
    },
    initialPageParam: 0,
    getPreviousPageParam: (firstPage) => firstPage.previousId ?? undefined,
    getNextPageParam: (lastPage) => lastPage.nextId ?? undefined,
    maxPages: 3,
  }))

  nextButtonDisabled = computed(
    () => !this.#hasNextPage() || this.#isFetchingNextPage(),
  )
  nextButtonText = computed(() =>
    this.#isFetchingNextPage()
      ? 'Loading more...'
      : this.#hasNextPage()
        ? 'Load newer'
        : 'Nothing more to load',
  )

  #hasNextPage = this.query.hasNextPage
  #isFetchingNextPage = this.query.isFetchingNextPage
}
```

```angular-html
<div>
  @if (query.isPending()) {
    <p>Loading...</p>
  } @else if (query.isError()) {
    <span>Error: {{ query?.error().message }}</span>
  } @else {
    @for (page of query?.data().pages; track $index) {
      @for (project of page.data; track project.id) {
        <p>{{ project.name }} {{ project.id }}</p>
      }
    }
    <div>
      <button (click)="query.fetchNextPage()" [disabled]="nextButtonDisabled()">
        {{ nextButtonText() }}
      </button>
    </div>
  }
</div>
```

[//]: # 'Example'
[//]: # 'Example1'

```angular-ts
@Component({
  template: ` <list-component (endReached)="fetchNextPage()" /> `,
})
export class Example {
  query = injectInfiniteQuery(() => ({
    queryKey: ['projects'],
    queryFn: async ({ pageParam }) => {
      return lastValueFrom(this.projectsService.getProjects(pageParam))
    },
  }))

  fetchNextPage() {
    // Do nothing if already fetching
    if (this.query.isFetching()) return
    this.query.fetchNextPage()
  }
}
```

[//]: # 'Example1'
[//]: # 'Example3'

```ts
query = injectInfiniteQuery(() => ({
  queryKey: ['projects'],
  queryFn: fetchProjects,
  getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
  getPreviousPageParam: (firstPage, pages) => firstPage.prevCursor,
}))
```

[//]: # 'Example3'
[//]: # 'Example4'

```ts
query = injectInfiniteQuery(() => ({
  queryKey: ['projects'],
  queryFn: fetchProjects,
  select: (data) => ({
    pages: [...data.pages].reverse(),
    pageParams: [...data.pageParams].reverse(),
  }),
}))
```

[//]: # 'Example4'
[//]: # 'Example8'

```ts
injectInfiniteQuery(() => ({
  queryKey: ['projects'],
  queryFn: fetchProjects,
  initialPageParam: 0,
  getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
  getPreviousPageParam: (firstPage, pages) => firstPage.prevCursor,
  maxPages: 3,
}))
```

[//]: # 'Example8'
[//]: # 'Example9'

```ts
injectInfiniteQuery(() => ({
  queryKey: ['projects'],
  queryFn: fetchProjects,
  initialPageParam: 0,
  getNextPageParam: (lastPage, allPages, lastPageParam) => {
    if (lastPage.length === 0) {
      return undefined
    }
    return lastPageParam + 1
  },
  getPreviousPageParam: (firstPage, allPages, firstPageParam) => {
    if (firstPageParam <= 1) {
      return undefined
    }
    return firstPageParam - 1
  },
}))
```

[//]: # 'Example9'
