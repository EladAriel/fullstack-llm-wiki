---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/cosh.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $cosh (expression operator)

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the input argument resolves to a value of `null` or refers to a field that is missing, :expression:`$cosh` returns `null`. If the argument resolves to `NaN`, :expression:`$cosh` returns `NaN`. If the argument resolves to negative or positive `Infinity`, :expression:`$cosh` returns positive `Infinity`.

## Example
