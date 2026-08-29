---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/ValueAccessor.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.388257Z"
---
# Valueaccessor

---
id: ValueAccessor
title: ValueAccessor
---

```ts
type ValueAccessor<T> = () => T & object;
```

Defined in: [packages/lit-query/src/accessor.ts:32](https://github.com/TanStack/query/blob/main/packages/lit-query/src/accessor.ts#L32)

A callable accessor with a `current` property for reading the latest
controller result.

Controller creators and cache state helpers return this shape so render code
can use either `result()` or `result.current`.

## Type Declaration

### current

```ts
readonly current: T;
```

## Type Parameters

### T

`T`

## Example

```ts
const query = this.todos()
const sameQuery = this.todos.current
```
