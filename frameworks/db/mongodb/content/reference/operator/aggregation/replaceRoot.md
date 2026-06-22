---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/replaceRoot.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $replaceRoot (aggregation stage)

## Definition

## Behavior

If the `<replacementDocument>` is not a document, :pipeline:`$replaceRoot` errors and fails.

If the `<replacementDocument>` resolves to a missing document (i.e. the document does not exist), :pipeline:`$replaceRoot` errors and fails. For example, create a collection with the following documents:

```javascript
db.collection.insertMany([
   { "_id": 1, "name" : { "first" : "John", "last" : "Backus" } },
   { "_id": 2, "name" : { "first" : "John", "last" : "McCarthy" } },
   { "_id": 3, "name": { "first" : "Grace", "last" : "Hopper" } },
   { "_id": 4, "firstname": "Ole-Johan", "lastname" : "Dahl" },
])
```

Then the following :pipeline:`$replaceRoot` operation fails because one of the documents does not have the `name` field:

```javascript
db.collection.aggregate([
   { $replaceRoot: { newRoot: "$name" } }
])
```

To avoid the error, you can use :expression:`$mergeObjects` to merge the `name` document into some default document; for example:

```javascript
db.collection.aggregate([
   { $replaceRoot: { newRoot: { $mergeObjects: [ { _id: "$_id", first: "", last: "" }, "$name" ] } } }
])
```

Alternatively, you can skip the documents that are missing the `name` field by including a :pipeline:`$match` stage to check for existence of the document field before passing documents to the :pipeline:`$replaceRoot` stage:

```javascript
db.collection.aggregate([
   { $match: { name : { $exists: true, $not: { $type: "array" }, $type: "object" } } },
   { $replaceRoot: { newRoot: "$name" } }
])
```

Or, you can use :expression:`$ifNull` expression to specify some other document to be root; for example:

```javascript
db.collection.aggregate([
   { $replaceRoot: { newRoot: { $ifNull: [ "$name", { _id: "$_id", missingName: true} ] } } }
])
```

## Examples

## Learn More

To learn more about related pipeline stages, see the :pipeline:`$replaceRoot` guide.
