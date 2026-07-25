---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/number-field/number-field.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.915149Z"
---
---
productId: material-ui
title: Number field React component
components: Button, IconButton, InputLabel, FormControl, FormLabel, FormHelperText, OutlinedInput
---

# Number Field

<p class="description">A React component for capturing numeric input from users.</p>

{{"component": "@mui/internal-core-docs/ComponentLinkHeader"}}

A number field is an input with increment and decrement buttons for capturing numeric input from users.

Material UI does not include a number field component out of the box, but this page provides components composed with the [Base UI `NumberField`](https://base-ui.com/react/components/number-field) and styled to align with Material Design (MD2) specifications, so they can be used with Material UI.

As such, you must install Base UI before proceeding.
The examples that follow can then be copied and pasted directly into your app.
Note that Base UI is tree-shakeable, so the final bundle will only include the components used in your project.

## Installation

<codeblock storageKey="package-manager">

```bash npm
npm install @base-ui/react
```

```bash pnpm
pnpm add @base-ui/react
```

```bash yarn
yarn add @base-ui/react
```

</codeblock>

## Usage

1. Select one of the demos below that fits your visual design needs.
2. Click **Expand code** in the toolbar.
3. Select the file that starts with `./components/`.
4. Copy the code and paste it into your project.

## Outlined field

The outlined field uses the same building-block components as Material UI's outlined `TextField`—`FormControl`, `OutlinedInput`, `InputLabel`, and `FormHelperText`—with end adornments for the increment and decrement buttons.
See [Text Field—Components](/material-ui/react-text-field/#components) for more details.

{{"demo": "FieldDemo.js"}}

## Spinner field

For the spinner field component, the increment and decrement buttons are placed next to the outlined input.
This is ideal for touch devices and narrow ranges of values.

{{"demo": "SpinnerDemo.js"}}

## Base UI API

See the documentation below for a complete reference to all of the props.

- [`NumberField`](https://base-ui.com/react/components/number-field#api-reference)
