---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/06-2025/06-13-2025-session-filtering.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.905182Z"
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