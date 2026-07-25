---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/reference/environmentManager.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: EnvironmentManager
title: environmentManager
---

The `environmentManager` manages how TanStack Query detects whether the current runtime should be treated as server-side.

By default, it uses the same server detection as the exported `isServer` utility from query-core.

Use this manager to override server detection globally for runtimes that are not traditional browser/server environments (for example, extension workers).

Its available methods are:

- [`isServer`](#environmentmanagerisserver)
- [`setIsServer`](#environmentmanagersetisserver)

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
