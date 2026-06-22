---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/agg-dollar-sign.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:**  When you use an aggregation pipeline, sanitize any strings that are passed from user
 input or created dynamically from parsing data. If any field values are literal string
 values and start with a dollar character, the value must be passed to the
 :expression:`$literal` aggregation operator. The following example demonstrates using
 the aggregation pipeline `$set` and the `$literal` operator to update the document
 with an `_id` of `1` to have a `cost` field of `$27`.
 .. code-block:: javascript
    db.inventory.updateOne( { _id: 1 }, [ { $set: { "cost": { $literal: "$27" } } } ] )
