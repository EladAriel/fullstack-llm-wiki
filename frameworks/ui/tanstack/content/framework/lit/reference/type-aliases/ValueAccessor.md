---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/ValueAccessor.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: ValueAccessor
title: ValueAccessor
---

# Type Alias: ValueAccessor\<T\>

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
