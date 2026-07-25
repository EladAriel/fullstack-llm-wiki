---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2026/04-28-2026-session-notes-api.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.883035Z"
---
# 04 28 2026 Session Notes Api

---
title: "04.28.2026 Session Notes API"
description: "Add session notes through a dedicated REST endpoint and reserve the note annotation name for session note APIs."
---

## Session Notes API

**Available in arize-phoenix 14.16.0+**

Phoenix now supports creating session notes through `POST /v1/session_notes`, giving session-level review workflows the same note-specific REST pattern used by traces and spans.

To keep note behavior consistent across APIs, the reserved annotation name `note` is no longer accepted on the generic session annotation endpoint. Use the dedicated note endpoint instead:

- `POST /v1/session_notes` for session notes
- `POST /v1/session_annotations` for regular session annotations
