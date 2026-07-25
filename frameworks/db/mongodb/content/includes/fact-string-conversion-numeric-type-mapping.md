---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-string-conversion-numeric-type-mapping.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- Integers within the 32-bit signed range become `int`.
- Integers outside the 32-bit range but within the 64-bit signed range
become `long`.

- Integers outside the 64-bit signed range become `double`, which can
result in loss of precision.

- Numbers with a decimal point or exponent notation become `double`.
