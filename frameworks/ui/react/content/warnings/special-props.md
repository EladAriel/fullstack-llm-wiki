---
type: "Framework Learn Page"
framework: "React"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/warnings/special-props.md"
source_commit: "7c36f7ac329fe3cf2e11222edce9a535158c2cab"
source_commit_short: "7c36f7a"
source_commit_date: "2026-08-24T10:33:57-07:00"
generated_at: "2026-08-29T09:40:25.475260Z"
---
# Special Props

---
title: Special Props Warning
---

Most props on a JSX element are passed on to the component, however, there are two special props (`ref` and `key`) which are used by React, and are thus not forwarded to the component.

For instance, you can't read `props.key` from a component. If you need to access the same value within the child component, you should pass it as a different prop (ex: `<ListItemWrapper key={result.id} id={result.id} />` and read `props.id`). While this may seem redundant, it's important to separate app logic from hints to React.
