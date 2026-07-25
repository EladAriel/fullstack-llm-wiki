---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/atan.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================

# $atan (expression operator)

## Behavior

### `null` and `NaN`

If the argument resolves to a value of `null` or refers to a field that is missing, :expression:`$atan` returns `null`. If the argument resolves to `NaN`, :expression:`$tan` returns `NaN`.

## Example
