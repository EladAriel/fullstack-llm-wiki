---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/guides/cookbooks/labeling-request-data.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.281065Z"
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
