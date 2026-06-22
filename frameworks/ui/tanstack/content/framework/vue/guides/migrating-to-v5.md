---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/vue/guides/migrating-to-v5.md"
source_commit: "4f11927ac5f3841984389a07587ee2ae1e0abfbb"
source_commit_short: "4f11927a"
source_commit_date: "2026-06-19T13:43:35+02:00"
generated_at: "2026-06-21T12:31:28Z"
---

---
id: migrating-to-tanstack-query-5
title: Migrating to TanStack Query v5
ref: docs/framework/react/guides/migrating-to-v5.md
---

[//]: # 'FrameworkSpecificBreakingChanges'

## Vue Query Breaking Changes

### `useQueries` composable returns `ref` instead of `reactive`

To fix compatibility with Vue 2, `useQueries` composable now returns `queries` array wrapped in `ref`.
Previously `reactive` was returned which led to multiple problems:

- User could spread return value loosing reactivity.
- `readonly` wrapper used for return value was breaking Vue 2 reactivity detection mechanism. This was a silent issue in Vue 2.6, but appeared as error in Vue 2.7.
- Vue 2 does not support arrays as a root value of `reactive`.

With this change all of those issues are fixed.

Also this aligns `useQueries` with other composables which return all of the values as `refs`.

### Vue v3.3 is now required

To be able to provide new features following Vue releases, we now require Vue 3 to be at least in v3.3 version.
Requirements for Vue 2.x remain unchanged.

[//]: # 'FrameworkSpecificBreakingChanges'
[//]: # 'FrameworkSpecificNewFeatures'

### Ability to run `vue-query` composables in `injectionContext`

Previously `vue-query` composables could be run only within `setup` function of the component.  
We had an escape hatch in place to allow those hooks to be run anywhere if user would provide `queryClient` as a composable option.

Now you can use `vue-query` composables in any function that supports `injectionContext`. Ex. router navigation guards.
When using this new feature, make sure that `vue-query` composable is running within `effectScope`. Otherwise it might lead to memory leaks.
We have added `dev-only` warnings to inform users about potential misusage.

[//]: # 'FrameworkSpecificNewFeatures'
