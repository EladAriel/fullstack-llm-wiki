---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/06-2025/06-12-2025-dataset-filtering.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.904514Z"
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