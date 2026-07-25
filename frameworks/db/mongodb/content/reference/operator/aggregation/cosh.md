---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/cosh.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================

# $cosh (expression operator)

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the input argument resolves to a value of `null` or refers to a field that is missing, :expression:`$cosh` returns `null`. If the argument resolves to `NaN`, :expression:`$cosh` returns `NaN`. If the argument resolves to negative or positive `Infinity`, :expression:`$cosh` returns positive `Infinity`.

## Example
