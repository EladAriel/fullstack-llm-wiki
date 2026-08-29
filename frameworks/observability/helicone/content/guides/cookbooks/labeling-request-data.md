---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/guides/cookbooks/labeling-request-data.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.332169Z"
---
---
title: "How to Label Your Request Data"
sidebarTitle: "Labeling Requests"
description: "Label your request data to make it easier to search and filter in Helicone. Learn about custom properties, feedback, and scores."
"twitter:title": "How to Label Your Request Data - Helicone OSS LLM Observability"
---

# Overview

In this guide you will learn how to label your request data. Then we will show you how you can filter on your labels request data in the dashboard.

There are 3 main different types of labeling you can do in Helicone.

1. Custom Properties
2. Feedback
3. Scores

Each of these labels have different implications and use cases. We will go through each of them in detail.

## Where you can attach labels to

You can attach a label to any request id.

## Custom Properties

Custom properties are key value pairs that you can attach to your request data. This can be useful for adding metadata to your request data. For example you can add a custom property to your request data to indicate the environment a request was made in (e.g. production, staging, development).
