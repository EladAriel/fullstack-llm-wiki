---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-string-conversion-numeric-type-mapping.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- Integers within the 32-bit signed range become `int`.
- Integers outside the 32-bit range but within the 64-bit signed range
become `long`.

- Integers outside the 64-bit signed range become `double`, which can
result in loss of precision.

- Numbers with a decimal point or exponent notation become `double`.
