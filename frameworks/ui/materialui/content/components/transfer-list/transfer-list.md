---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/transfer-list/transfer-list.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.957489Z"
---
---
productId: material-ui
title: Transfer list React component
components: List, ListItem, Checkbox, Switch
githubLabel: 'scope: transfer list'
---

# Transfer List

<p class="description">A Transfer List (or "shuttle") enables the user to move one or more list items between lists.</p>

{{"component": "@mui/internal-core-docs/ComponentLinkHeader"}}

## Basic transfer list

For completeness, this example includes buttons for "move all", but not every transfer list needs these.

{{"demo": "TransferList.js", "bg": true}}

## Enhanced transfer list

This example exchanges the "move all" buttons for a "select all / select none" checkbox and adds a counter.

{{"demo": "SelectAllTransferList.js", "bg": true}}

## Limitations

The component comes with a couple of limitations:

- It only works on desktop.
  If you have a limited amount of options to select, prefer the [Autocomplete](/material-ui/react-autocomplete/#multiple-values) component.
  If mobile support is important for you, have a look at [#27579](https://github.com/mui/material-ui/issues/27579).
- There are no high-level components exported from npm. The demos are based on composition.
  If this is important for you, have a look at [#27579](https://github.com/mui/material-ui/issues/27579).
