---
type: "Framework Learn Page"
framework: "TanStack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/lit/reference/type-aliases/Accessor.md"
source_commit: "2969edf32f7e0c48e2a108d84712d6e01edfde21"
source_commit_short: "2969edf"
source_commit_date: "2026-08-28T01:03:02+09:00"
generated_at: "2026-08-29T09:40:33.390251Z"
---
# Accessor

---
id: Accessor
title: Accessor
---

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
