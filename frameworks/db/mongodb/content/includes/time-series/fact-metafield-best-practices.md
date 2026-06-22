---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-metafield-best-practices.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- Select fields that rarely or never change as part of your metaField.
- If possible, select identifiers or other stable values that are common in filter
expressions as part of your metaField.

- Avoid selecting fields that are not used for filtering as part of your
metaField. Instead, use those fields as measurements.
