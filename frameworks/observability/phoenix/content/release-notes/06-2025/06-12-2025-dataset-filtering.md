---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/06-2025/06-12-2025-dataset-filtering.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.855779Z"
---
# 06 12 2025 Dataset Filtering

---
title: "06.12.2025: Dataset filtering"
description: Available in Phoenix 10.11+
---

<Update label="06.12.2025">

## Dataset Filtering

<Frame>
    <iframe src="https://cdn.iframe.ly/D9lKIPd9" width={1000} height={400} allowFullScreen></iframe>
</Frame>

This release enables filtering of datasets by name across both the API and user interface, integrating a live search input along with support for pagination and sorting to improve data navigation and usability.

* Added a `DatasetFilter` input and enum to the GraphQL schema, allowing users to filter datasets by name using case-insensitive matching.
* Created a debounced `DatasetsSearch` component on the Datasets page that lets users filter results live as they type.

<Card title="feat: dataset-filter by GeLi2001 · Pull Request #7982 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/7982" horizontal>
  GitHub
</Card>
</Update>