---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/customization/z-index/z-index.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.974952Z"
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
