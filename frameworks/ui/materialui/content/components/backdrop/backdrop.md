---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/backdrop/backdrop.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.957016Z"
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
