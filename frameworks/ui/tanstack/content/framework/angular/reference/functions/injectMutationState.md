---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/angular/reference/functions/injectMutationState.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: injectMutationState
title: injectMutationState
---

# Function: injectMutationState()

```ts
function injectMutationState<TResult>(injectMutationStateFn, options?): Signal<TResult[]>;
```

Defined in: [inject-mutation-state.ts:60](https://github.com/TanStack/query/blob/main/packages/angular-query-experimental/src/inject-mutation-state.ts#L60)

Injects a signal that tracks the state of all mutations.

## Type Parameters

### TResult

`TResult` = `MutationState`\<`unknown`, `Error`, `unknown`, `unknown`\>

## Parameters

### injectMutationStateFn

() => `MutationStateOptions`\<`TResult`\>

A function that returns mutation state options.

### options?

[`InjectMutationStateOptions`](../interfaces/InjectMutationStateOptions.md)

The Angular injector to use.

## Returns

`Signal`\<`TResult`[]\>

The signal that tracks the state of all mutations.
