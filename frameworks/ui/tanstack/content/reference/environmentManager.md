---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/reference/environmentManager.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.357728Z"
---
# Environmentmanager

---
id: EnvironmentManager
title: environmentManager
---

The `environmentManager` manages how TanStack Query detects whether the current runtime should be treated as server-side.

By default, it uses the same server detection as the exported `isServer` utility from query-core.

Use this manager to override server detection globally for runtimes that are not traditional browser/server environments (for example, extension workers).

Its available methods are:

- [`isServer`](#environmentmanager-isserver)
- [`setIsServer`](#environmentmanager-setisserver)

## `environmentManager.isServer`

Returns whether the current runtime is treated as a server environment.

```tsx
import { environmentManager } from '@tanstack/react-query'

const server = environmentManager.isServer()
```

## `environmentManager.setIsServer`

Overrides the server check globally.

```tsx
import { environmentManager } from '@tanstack/react-query'

// Override
environmentManager.setIsServer(() => {
  return typeof window === 'undefined' && !('chrome' in globalThis)
})
```

**Options**

- `isServerValue: () => boolean`

To restore the default behavior, set the function back to query-core's `isServer` utility:

```tsx
import { environmentManager, isServer } from '@tanstack/react-query'

environmentManager.setIsServer(() => isServer)
```
