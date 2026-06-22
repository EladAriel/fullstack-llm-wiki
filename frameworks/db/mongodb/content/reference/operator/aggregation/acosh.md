---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/acosh.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $acosh (expression operator)

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the argument resolves to a value of `null` or refers to a field that is missing, :expression:`$acosh` returns `null`. If the argument resolves to `NaN`, :expression:`$acosh` returns `NaN`. If the argument resolves to negative infinity,  :expression:`$acosh` throws an error. If the argument resolves to `Infinity`, :expression:`$acosh` returns `Infinity`.  If the argument resolves to a value outside the bounds of  `[-1, Infinity]` inclusive, :expression:`$acosh` throws an error.

## Example
