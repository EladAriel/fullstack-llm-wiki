---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/Accessor.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
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
