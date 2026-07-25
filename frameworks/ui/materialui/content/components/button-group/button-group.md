---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/button-group/button-group.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.934739Z"
---
---
productId: material-ui
title: React Button Group component
components: Button, ButtonGroup
githubLabel: 'component: ButtonGroup'
githubSource: packages/mui-material/src/ButtonGroup
---

# Button Group

<p class="description">The ButtonGroup component can be used to group related buttons.</p>

{{"component": "@mui/internal-core-docs/ComponentLinkHeader"}}

## Basic button group

The buttons can be grouped by wrapping them with the `ButtonGroup` component.
They need to be immediate children.

{{"demo": "BasicButtonGroup.js"}}

## Button variants

All the standard button variants are supported.

{{"demo": "VariantButtonGroup.js"}}

## Sizes and colors

The `size` and `color` props can be used to control the appearance of the button group.

{{"demo": "GroupSizesColors.js"}}

## Vertical group

The button group can be displayed vertically using the `orientation` prop.

{{"demo": "GroupOrientation.js"}}

## Split button

`ButtonGroup` can also be used to create a split button. The dropdown can change the button action (as in this example) or be used to immediately trigger a related action.

{{"demo": "SplitButton.js"}}

## Disabled elevation

You can remove the elevation with the `disableElevation` prop.

{{"demo": "DisableElevation.js"}}

## Loading

Use the `loading` prop from `Button` to set buttons in a loading state and disable interactions.

{{"demo": "LoadingButtonGroup.js"}}
