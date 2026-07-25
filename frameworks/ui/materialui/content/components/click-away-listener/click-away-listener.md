---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/click-away-listener/click-away-listener.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.960018Z"
---
---
productId: material-ui
title: Detect click outside React component
components: ClickAwayListener
githubLabel: 'scope: click away listener'
---

# Click-Away Listener

<p class="description">The Click-Away Listener component detects when a click event happens outside of its child element.</p>

{{"component": "@mui/internal-core-docs/ComponentLinkHeader", "design": false}}

## Introduction

Click-Away Listener is a utility component that listens for click events outside of its child.
(Note that it only accepts _one_ child element.)
This is useful for components like the [Popper](/material-ui/react-popper/) which should close when the user clicks anywhere else in the document.
Click-Away Listener also supports the [Portal](/material-ui/react-portal/) component.

The demo below shows how to hide a menu dropdown when users click anywhere else on the page:

{{"demo": "ClickAway.js"}}

## Basics

### Import

```jsx
import ClickAwayListener from '@mui/material/ClickAwayListener';
```

## Customization

### Use with Portal

The following demo uses the [Portal](/material-ui/react-portal/) component to render the dropdown into a new subtree outside of the current DOM hierarchy:

{{"demo": "PortalClickAway.js"}}

### Listening for leading events

By default, the Click-Away Listener component responds to **trailing events**—the _end_ of a click or touch.

You can set the component to listen for **leading events** (the start of a click or touch) using the `mouseEvent` and `touchEvent` props, as shown in the following demo:

:::warning
When the component is set to listen for leading events, interactions with the scrollbar are ignored.
:::

{{"demo": "LeadingClickAway.js"}}

## Accessibility

By default, Click-Away Listener adds an `onClick` handler to its child.
This can result in screen readers announcing that the child is clickable, even though this `onClick` handler has no effect on the child itself.

To prevent this behavior, add `role="presentation"` to the child element:

```tsx
<ClickAwayListener>
  <div role="presentation">
    <h1>non-interactive heading</h1>
  </div>
</ClickAwayListener>
```

This is also required to fix a known issue in NVDA when using Firefox that prevents the announcement of alert messages—see [this GitHub issue](https://github.com/mui/material-ui/issues/29080) for details.
