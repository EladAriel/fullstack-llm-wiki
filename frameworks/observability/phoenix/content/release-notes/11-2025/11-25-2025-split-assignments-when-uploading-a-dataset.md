---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/11-2025/11-25-2025-split-assignments-when-uploading-a-dataset.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.845689Z"
---
# 11 25 2025 Split Assignments When Uploading A Dataset

---
title: "11.25.2025: Split Assignments When Uploading a Dataset"
description: Available in Phoenix 12.18+
---

<Frame>
  <video src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/upload-dataset-splits.mp4" controls style={{ width: '100%' }} />
</Frame>

With this update, Phoenix supports providing split labels during dataset upload — so you don't have to assign splits manually after uploading.

Once uploaded, you can immediately filter, query, or use those splits in experiments and evaluations. This streamlines data-preparation workflows and removes an extra manual step when organizing datasets for training, evaluation, or analysis.

<Card title="Pull Request #10353" href="https://github.com/Arize-ai/phoenix/pull/10353" icon="github" horizontal>
GitHub
</Card>
