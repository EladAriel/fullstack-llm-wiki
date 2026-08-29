---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/no-ssr/no-ssr.md"
source_commit: "fc3a3a0a8b7c8f20274eca4758ea07a33e25c1b4"
source_commit_short: "fc3a3a0a"
source_commit_date: "2026-08-28T09:03:39+07:00"
generated_at: "2026-08-29T09:40:18.221607Z"
---
---
productId: material-ui
title: No SSR React component
components: NoSsr
---

# No SSR

<p class="description">The No-SSR component defers the rendering of children components from the server to the client.</p>

{{"component": "@mui/internal-core-docs/ComponentLinkHeader", "design": false}}

## Introduction

No-SSR is a utility component that prevents its children from being rendered on the server, deferring their rendering to the client instead.
This can be useful in a variety of situations, including:

- To create an escape hatch for broken dependencies that don't support server-side rendering (SSR)
- To improve the time to first paint by only rendering above the fold
- To reduce the rendering time on the server
- To turn on service degradation when the server load is too heavy
- To improve the Time to Interactive (TTI) by only rendering what's important (using the `defer` prop)

The demo below illustrates how this component works:

{{"demo": "SimpleNoSsr.js"}}

## Basics

### Import

```jsx
import NoSsr from '@mui/material/NoSsr';
```

## Customization

### Delay client-side rendering

You can also use No-SSR to delay the rendering of specific components on the client-side—for example, to let the rest of the application load before an especially complex or data-heavy component.

The following demo shows how to use the `defer` prop to prioritize rendering the rest of the app outside of what is nested within No-SSR:

{{"demo": "FrameDeferring.js"}}

:::warning
When using No-SSR in this way, React applies [two commits](https://react.dev/learn/render-and-commit) instead of one.
:::
