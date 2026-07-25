---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/replaceWith.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================

# $replaceWith (aggregation stage)

## Definition

## Behavior

If the `<replacementDocument>` is not a document, :pipeline:`$replaceWith` errors and fails.

If the `<replacementDocument>` resolves to a missing document (i.e. the document does not exist), :pipeline:`$replaceWith` errors and fails. For example, create a collection with the following documents:

Then the following :pipeline:`$replaceWith` operation fails because one of the document does not have the `name` field:

```javascript
db.collection.aggregate([
   { $replaceWith: "$name" }
])
```

To avoid the error, you can use :expression:`$mergeObjects` to merge the  `name` document with some default document; for example:

Alternatively, you can skip the documents that are missing the `name` field by including a :pipeline:`$match` stage to check for existence of the document field before passing documents to the :pipeline:`$replaceWith` stage:

Or, you can use :expression:`$ifNull` expression to specify some other document to be root; for example:

## Examples

## Learn More

To learn more about related pipeline stages, see the :pipeline:`$replaceRoot` guide.
