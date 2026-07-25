---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-timezone-description-no-option.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The timezone to carry out the operation. `<tzExpression>` must be a valid `expression <aggregation-expressions>` that resolves to a string formatted as either an [Olson Timezone Identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) or a [UTC Offset](https://en.wikipedia.org/wiki/List_of_UTC_time_offsets):

- Olson Timezone Identifier: for example, `"America/New_York"`,
`"Europe/London"`, `"GMT"`

- UTC Offset: for example, `"+04:45"`, `"-0530"`, `"+03"`
If you omit `timezone`, the result is displayed in `UTC`.
