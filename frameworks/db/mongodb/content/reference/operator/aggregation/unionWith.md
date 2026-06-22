---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/unionWith.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $unionWith (aggregation stage)

## Definition

## Syntax

The `$unionWith` stage has the following syntax:

```javascript
{ $unionWith: { coll: "<collection>", pipeline: [ <stage1>, ... ] } }
```

To include all documents from the specified collection without any processing, you can use the simplified form:

```javascript
{ $unionWith: "<collection>" }  // Include all documents from the specified collection
```

The `$unionWith` stage takes a document with the following fields:

The :pipeline:`$unionWith` operation would correspond to the following SQL statement:

```sql
SELECT *
FROM Collection1
WHERE ...
UNION ALL
SELECT *
FROM Collection2
WHERE ...
```

## Considerations

### Duplicate Results

The combined results from the previous stage and the :pipeline:`$unionWith` stage can include duplicates.

For example, create a `suppliers` collection and a `warehouses` collection:

```javascript
db.suppliers.insertMany([
  { _id: 1, supplier: "Aardvark and Sons", state: "Texas" },
  { _id: 2, supplier: "Bears Run Amok.", state: "Colorado"},
  { _id: 3, supplier: "Squid Mark Inc. ", state: "Rhode Island" },
])
```

```javascript
db.warehouses.insertMany([
  { _id: 1, warehouse: "A", region: "West", state: "California" },
  { _id: 2, warehouse: "B", region: "Central", state: "Colorado"},
  { _id: 3, warehouse: "C", region: "East", state: "Florida" },
])
```

The following aggregation combines the `state` field projection results from the `suppliers` and `warehouse` collections.

```javascript
db.suppliers.aggregate([
   { $project: { state: 1, _id: 0 } },
   { $unionWith: { coll: "warehouses", pipeline: [ { $project: { state: 1, _id: 0 } } ]} }
])
```

The result set contains duplicates:

```javascript
{ "state" : "Texas" }
{ "state" : "Colorado" }
{ "state" : "Rhode Island" }
{ "state" : "California" }
{ "state" : "Colorado" }
{ "state" : "Florida" }
```

To remove the duplicates, you can include a :pipeline:`$group` stage to group by the `state` field:

```javascript
db.suppliers.aggregate([
   { $project: { state: 1, _id: 0 } },
   { $unionWith: { coll: "warehouses", pipeline: [ { $project: { state: 1, _id: 0 } } ]} },
   { $group: { _id: "$state" } }
])
```

The result set no longer contains duplicates:

```javascript
{ "_id" : "California" }
{ "_id" : "Texas" }
{ "_id" : "Florida" }
{ "_id" : "Colorado" }
{ "_id" : "Rhode Island" }
```

### Collation

If the :method:`db.collection.aggregate()` includes a `collation` document, the operation uses that collation and ignores any other collations.

If the :method:`db.collection.aggregate()` does not include a `collation` document, the :method:`db.collection.aggregate()` method uses the collation for the top-level collection/view on which the :method:`db.collection.aggregate()` is run:

- If the `$unionWith coll <unionWith-coll>` is a collection, its
collation is ignored.

- If the `$unionWith coll <unionWith-coll>` is a :doc:`view
</core/views>`, then its collation must match that of the top-level collection/view.  Otherwise, the operation errors.

### {+fts+} Support

Starting in MongoDB 6.0, you can specify the :atlas:`{+fts+} </atlas-search>` :pipeline:`$search` or :pipeline:`$searchMeta` stage in the `$unionWith` pipeline to search collections on the Atlas cluster. The :pipeline:`$search` or the :pipeline:`$searchMeta` stage must be the first stage inside the `$unionWith` pipeline.

To see an example of :pipeline:`$unionWith` with :pipeline:`$search`, see the {+fts+} tutorial :atlas:`Run a {+fts+} $search Query Using $unionWith </atlas-search/tutorial/search-with-unionwith/>`.

### Restrictions

## Examples
