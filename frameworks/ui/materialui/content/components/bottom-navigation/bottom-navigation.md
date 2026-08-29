---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/bottom-navigation/bottom-navigation.md"
source_commit: "fc3a3a0a8b7c8f20274eca4758ea07a33e25c1b4"
source_commit_short: "fc3a3a0a"
source_commit_date: "2026-08-28T09:03:39+07:00"
generated_at: "2026-08-29T09:40:18.234695Z"
---
---
productId: material-ui
title: Bottom Navigation React component
components: BottomNavigation, BottomNavigationAction
githubLabel: 'scope: bottom navigation'
materialDesign: https://m2.material.io/components/bottom-navigation
githubSource: packages/mui-material/src/BottomNavigation
---

# Bottom Navigation

<p class="description">The Bottom Navigation bar allows movement between primary destinations in an app.</p>

Bottom navigation bars display three to five destinations at the bottom of a screen. Each destination is represented by an icon and an optional text label. When a bottom navigation icon is tapped, the user is taken to the top-level navigation destination associated with that icon.

{{"component": "@mui/internal-core-docs/ComponentLinkHeader"}}

## Bottom navigation

When there are only **three** actions, display both icons and text labels at all times.

{{"demo": "SimpleBottomNavigation.js", "bg": true}}

## Bottom navigation with no label

If there are **four** or **five** actions, display inactive views as icons only.

{{"demo": "LabelBottomNavigation.js", "bg": true}}

## Fixed positioning

This demo keeps bottom navigation fixed to the bottom, no matter the amount of content on-screen.

{{"demo": "FixedBottomNavigation.js", "bg": true, "iframe": true, "maxWidth": 600}}

## Third-party routing library

One frequent use case is to perform navigation on the client only, without an HTTP round-trip to the server.
The `BottomNavigationAction` component provides the `component` prop to handle this use case.
Here is a [more detailed guide](/material-ui/integrations/routing/).
