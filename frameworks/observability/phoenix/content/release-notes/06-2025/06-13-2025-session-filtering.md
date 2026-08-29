---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/06-2025/06-13-2025-session-filtering.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.856520Z"
---
# 06 13 2025 Session Filtering

---
title: "06.13.2025: Session filtering"
description: Available in Phoenix 10.12+
---

<Update label="06.13.2025">

## Session Filtering

<Frame>
    <iframe src="https://cdn.iframe.ly/mYd4HURy" width={1000} height={400} allowFullScreen></iframe>
</Frame>

**New Features:**

* Added an optional `sessionId` argument to the `Project.sessions` GraphQL field, enabling filtering by `session_id`.
* Integrated support across the backend resolver and frontend UI to seamlessly filter and display sessions matching a specific `session_id`.

<Card title="feat: allow filtering of sessions by session_id by RogerHYang · Pull Request #8038 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/8038" horizontal>
  GitHub
</Card>
</Update>