---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/atan2.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $atan2 (expression operator)

## Behavior

### `null` and `NaN`

If either argument given to `$atan2` is `null`, the expression returns `null`.  If either argument is `NaN`, the expression returns `NaN`. If one argument is `null` and the other is `NaN`, the expression returns `null`.

## Example
