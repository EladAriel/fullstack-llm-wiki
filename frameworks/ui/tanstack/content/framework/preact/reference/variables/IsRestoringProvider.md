---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/preact/reference/variables/IsRestoringProvider.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.375906Z"
---
# Isrestoringprovider

---
id: IsRestoringProvider
title: IsRestoringProvider
---

```ts
const IsRestoringProvider: Provider<boolean> = IsRestoringContext.Provider;
```

Defined in: [preact-query/src/IsRestoringProvider.ts:19](https://github.com/TanStack/query/blob/main/packages/preact-query/src/IsRestoringProvider.ts#L19)

The Provider that `PersistQueryClientProvider` uses to signal whether a persisted client is currently
being restored, read by `useIsRestoring`.
