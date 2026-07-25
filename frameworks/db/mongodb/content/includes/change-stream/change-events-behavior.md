---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/change-events-behavior.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In MongoDB 8.2.0, |collectionUUID-link| and |disambiguatedPaths-link| are included in applicable change events even if you do not set `showExpandedEvents`. In MongoDB versions earlier than 8.2.0 and in versions 8.2.1 and later, these fields are included only if you open the change stream with `showExpandedEvents: true`.
