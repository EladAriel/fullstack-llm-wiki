---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/reference/focusManager.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.357418Z"
---
# Focusmanager

---
id: FocusManager
title: FocusManager
---

The `FocusManager` manages the focus state within TanStack Query.

It can be used to change the default event listeners or to manually change the focus state.

Its available methods are:

- [`setEventListener`](#focusmanager-seteventlistener)
- [`subscribe`](#focusmanager-subscribe)
- [`setFocused`](#focusmanager-setfocused)
- [`isFocused`](#focusmanager-isfocused)

## `focusManager.setEventListener`

`setEventListener` can be used to set a custom event listener:

```tsx
import { focusManager } from '@tanstack/react-query'

focusManager.setEventListener((handleFocus) => {
  // Listen to visibilitychange
  if (typeof window !== 'undefined' && window.addEventListener) {
    window.addEventListener('visibilitychange', handleFocus, false)
  }

  return () => {
    // Be sure to unsubscribe if a new handler is set
    window.removeEventListener('visibilitychange', handleFocus)
  }
})
```

## `focusManager.subscribe`

`subscribe` can be used to subscribe to changes in the visibility state. It returns an unsubscribe function:

```tsx
import { focusManager } from '@tanstack/react-query'

const unsubscribe = focusManager.subscribe((isVisible) => {
  console.log('isVisible', isVisible)
})
```

## `focusManager.setFocused`

`setFocused` can be used to manually set the focus state. Set `undefined` to fall back to the default focus check.

```tsx
import { focusManager } from '@tanstack/react-query'

// Set focused
focusManager.setFocused(true)

// Set unfocused
focusManager.setFocused(false)

// Fallback to the default focus check
focusManager.setFocused(undefined)
```

**Options**

- `focused: boolean | undefined`

## `focusManager.isFocused`

`isFocused` can be used to get the current focus state.

```tsx
const isFocused = focusManager.isFocused()
```
