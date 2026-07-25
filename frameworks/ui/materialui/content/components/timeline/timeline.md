---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/components/timeline/timeline.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.951186Z"
---
---
productId: material-ui
title: React Timeline component
components: Timeline, TimelineItem, TimelineSeparator, TimelineDot, TimelineConnector, TimelineContent, TimelineOppositeContent
githubLabel: 'scope: timeline'
packageName: '@mui/lab'
---

# Timeline

<p class="description">The timeline displays a list of events in chronological order.</p>

:::info
This component is not documented in the [Material Design guidelines](https://m2.material.io/), but it is available in Material UI.
:::

{{"component": "@mui/internal-core-docs/ComponentLinkHeader"}}

## Basic timeline

A basic timeline showing list of events.

{{"demo": "BasicTimeline.js"}}

## Left-positioned timeline

The main content of the timeline can be positioned on the left side relative to the time axis.

{{"demo": "LeftPositionedTimeline.js"}}

## Alternating timeline

The timeline can display the events on alternating sides.

{{"demo": "AlternateTimeline.js"}}

## Reverse Alternating timeline

The timeline can display the events on alternating sides in reverse order.

{{"demo": "AlternateReverseTimeline.js"}}

## Color

The `TimelineDot` can appear in different colors from theme palette.

{{"demo": "ColorsTimeline.js"}}

## Outlined

{{"demo": "OutlinedTimeline.js"}}

## Opposite content

The timeline can display content on opposite sides.

{{"demo": "OppositeContentTimeline.js"}}

## Customization

Here is an example of customizing the component.
You can learn more about this in the [overrides documentation page](/material-ui/customization/how-to-customize/).

{{"demo": "CustomizedTimeline.js"}}

## Alignment

There are different ways in which a Timeline can be placed within the container.

You can do it by overriding the styles.

A Timeline centers itself in the container by default.

The demos below show how to adjust the relative width of the left and right sides of a Timeline:

### Left-aligned

{{"demo": "LeftAlignedTimeline.js"}}

### Right-aligned

{{"demo": "RightAlignedTimeline.js"}}

### Left-aligned with no opposite content

{{"demo": "NoOppositeContent.js"}}
