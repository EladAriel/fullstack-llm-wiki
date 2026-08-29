---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/backdrop/backdrop.md"
source_commit: "fc3a3a0a8b7c8f20274eca4758ea07a33e25c1b4"
source_commit_short: "fc3a3a0a"
source_commit_date: "2026-08-28T09:03:39+07:00"
generated_at: "2026-08-29T09:40:18.232004Z"
---
---
productId: material-ui
title: Backdrop React Component
components: Backdrop
githubLabel: 'scope: backdrop'
githubSource: packages/mui-material/src/Backdrop
---

# Backdrop

<p class="description">The Backdrop component narrows the user's focus to a particular element on the screen.</p>

The Backdrop signals a state change within the application and can be used for creating loaders, dialogs, and more.
In its simplest form, the Backdrop component will add a dimmed layer over your application.

{{"component": "@mui/internal-core-docs/ComponentLinkHeader"}}

## Example

The demo below shows a basic Backdrop with a Circular Progress component in the foreground to indicate a loading state.
After clicking **Show Backdrop**, you can click anywhere on the page to close it.

{{"demo": "SimpleBackdrop.js"}}

## Transitions

Backdrop uses [Fade](/material-ui/transitions/#fade) by default.
Use `slots.transition` and `slotProps.transition` to replace it with another transition or to pass transition props.
