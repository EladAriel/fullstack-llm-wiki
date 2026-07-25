---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-positional-projection-vs-elemmatch.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Both the :projection:`$` operator and the :projection:`$elemMatch` operator project the **first** matching element from an array based on a condition.

The :projection:`$` operator projects the first matching array element from each document in a collection based on some condition from the query statement.

The :projection:`$elemMatch` projection operator takes an explicit condition argument.  This allows you to project based on a condition not in the query, or if you need to project based on multiple fields in the array's embedded documents. See `array-field-limitation` for an example.
