---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/agg-dollar-sign.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:**  When you use an aggregation pipeline, sanitize any strings that are passed from user
 input or created dynamically from parsing data. If any field values are literal string
 values and start with a dollar character, the value must be passed to the
 :expression:`$literal` aggregation operator. The following example demonstrates using
 the aggregation pipeline `$set` and the `$literal` operator to update the document
 with an `_id` of `1` to have a `cost` field of `$27`.
 .. code-block:: javascript
    db.inventory.updateOne( { _id: 1 }, [ { $set: { "cost": { $literal: "$27" } } } ] )
