---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/Accessor.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: Accessor
title: Accessor
---

# Type Alias: Accessor\<T\>

```ts
type Accessor<T> = T | () => T;
```

Defined in: [packages/lit-query/src/accessor.ts:13](https://github.com/TanStack/query/blob/main/packages/lit-query/src/accessor.ts#L13)

A value that can be passed directly or read from a zero-argument getter.

Lit Query APIs read function accessors during host updates, so the getter can
depend on reactive host state.

## Type Parameters

### T

`T`

## Example

```ts
const staticKey: Accessor<readonly unknown[]> = ['todos']
const reactiveKey: Accessor<readonly unknown[]> = () => ['todos', this.userId]
```
