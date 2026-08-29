---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/functions/useIsRestoring.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.372377Z"
---
# Useisrestoring

---
id: useIsRestoring
title: useIsRestoring
---

```ts
function useIsRestoring(): boolean;
```

Defined in: [preact-query/src/IsRestoringProvider.ts:13](https://github.com/TanStack/query/blob/main/packages/preact-query/src/IsRestoringProvider.ts#L13)

If you are using `PersistQueryClientProvider`, you can also use the `useIsRestoring` hook alongside it to
check if a restore is currently in progress. `useQuery` and friends also check this internally to avoid
race conditions between the restore and mounting queries.

## Returns

`boolean`

`true` while a persisted client is being restored, `false` otherwise.
