---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/asinh.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $asinh (expression operator)

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the argument resolves to a value of `null` or refers to a field that is missing, :expression:`$asinh` returns `null`. If the argument resolves to `NaN`, :expression:`$asinh` returns `NaN`. If the argument resolves to negative or positive infinity, :expression:`$asinh` returns negative or positive infinity respectively.

## Example
