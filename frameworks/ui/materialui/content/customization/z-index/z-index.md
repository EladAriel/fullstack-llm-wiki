---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/customization/z-index/z-index.md"
source_commit: "fc3a3a0a8b7c8f20274eca4758ea07a33e25c1b4"
source_commit_short: "fc3a3a0a"
source_commit_date: "2026-08-28T09:03:39+07:00"
generated_at: "2026-08-29T09:40:18.253939Z"
---
# z-index

<p class="description">z-index is the CSS property that helps control layout by providing a third axis to arrange content.</p>

Several Material UI components utilize `z-index`, employing a default z-index scale
that has been designed to properly layer drawers, modals, snackbars, tooltips, and more.

The `z-index` values start at an arbitrary number, high and specific enough to ideally avoid conflicts:

- mobile stepper: 1000
- fab: 1050
- speed dial: 1050
- app bar: 1100
- drawer: 1200
- modal: 1300
- snackbar: 1400
- tooltip: 1500

These values can always be customized.
You will find them in the theme under the [`zIndex`](/material-ui/customization/default-theme/?expand-path=$.zIndex) key of the theme.
Customization of individual values is discouraged; should you change one, you likely need to change them all.
