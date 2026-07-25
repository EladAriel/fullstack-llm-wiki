---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/getting-started/usage/usage.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.986574Z"
---
# Usage

<p class="description">Learn the basics of working with Material UI components.</p>

## Quickstart

After [installation](/material-ui/getting-started/installation/), you can import any Material UI component and start playing around.
For example, try changing the `variant` on the [Button](/material-ui/react-button/) to `outlined` to see how the style changes:

{{"demo": "ButtonUsage.js", "defaultCodeOpen": true}}

## Globals

Since Material UI components are built to function in isolation, they don't require any kind of globally scoped styles.
For a better user experience and developer experience, we recommend adding the following globals to your app.

### Responsive meta tag

Material UI is a _mobile-first_ component library—we write code for mobile devices first, and then scale up the components as necessary using CSS media queries.

To ensure proper rendering and touch zooming for all devices, add the responsive viewport meta tag to your `<head>` element:

```html
<meta name="viewport" content="initial-scale=1, width=device-width" />
```

### CssBaseline

Material UI provides an optional [CssBaseline](/material-ui/react-css-baseline/) component.
It fixes some inconsistencies across browsers and devices while providing resets that are better tailored to fit Material UI than alternative global style sheets like [normalize.css](https://github.com/necolas/normalize.css/).

### Default font

Material UI uses the Roboto font by default.
See [Installation—Roboto font](/material-ui/getting-started/installation/#roboto-font) for complete details.
