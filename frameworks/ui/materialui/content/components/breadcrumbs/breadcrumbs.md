---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/breadcrumbs/breadcrumbs.md"
source_commit: "fc3a3a0a8b7c8f20274eca4758ea07a33e25c1b4"
source_commit_short: "fc3a3a0a"
source_commit_date: "2026-08-28T09:03:39+07:00"
generated_at: "2026-08-29T09:40:18.223265Z"
---
---
productId: material-ui
title: React Breadcrumbs component
components: Breadcrumbs, Link, Typography
githubLabel: 'scope: breadcrumbs'
waiAria: https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/
githubSource: packages/mui-material/src/Breadcrumbs
---

# Breadcrumbs

<p class="description">A breadcrumbs is a list of links that help visualize a page's location within a site's hierarchical structure, it allows navigation up to any of the ancestors.</p>

{{"component": "@mui/internal-core-docs/ComponentLinkHeader"}}

## Basic breadcrumbs

{{"demo": "BasicBreadcrumbs.js"}}

## Active last breadcrumb

Keep the last breadcrumb interactive.

{{"demo": "ActiveLastBreadcrumb.js"}}

## Custom separator

In the following examples, we are using two string separators and an SVG icon.

{{"demo": "CustomSeparator.js"}}

## Breadcrumbs with icons

{{"demo": "IconBreadcrumbs.js"}}

## Collapsed breadcrumbs

{{"demo": "CollapsedBreadcrumbs.js"}}

## Condensed with menu

As an alternative, consider adding a Menu component to display the condensed links in a dropdown list:

{{"demo": "CondensedWithMenu.js"}}

## Customization

Here is an example of customizing the component.
You can learn more about this in the [overrides documentation page](/material-ui/customization/how-to-customize/).

{{"demo": "CustomizedBreadcrumbs.js"}}

## Integration with react-router

{{"demo": "RouterBreadcrumbs.js", "bg": true}}

## Accessibility

(WAI-ARIA: https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/)

Be sure to add a `aria-label` description on the `Breadcrumbs` component.

The accessibility of this component relies on:

- The set of links is structured using an ordered list (`<ol>` element).
- To prevent screen reader announcement of the visual separators between links, they are hidden with `aria-hidden`.
- A nav element labeled with `aria-label` identifies the structure as a breadcrumb trail and makes it a navigation landmark so that it is easy to locate.
