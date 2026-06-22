---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-wildcard.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================

# Wildcard Indexes

MongoDB supports creating indexes on a field, or set of fields, to improve performance for queries. MongoDB supports `flexible schemas <manual-data-modeling-intro>`, meaning document field names may differ within a collection. Use wildcard indexes to support queries against arbitrary or unknown fields.

To create a wildcard index, use the wildcard specifier (`$**`) as the index key:

```javascript
db.collection.createIndex( { "$**": <sortOrder> } )
```

You can use the following commands to create a wildcard index:

- :dbcommand:`createIndexes`
- :method:`db.collection.createIndex()`
- :method:`db.collection.createIndexes()`
## Use Cases

.. include:: /includes/indexes/wildcard-use-case-warning.rst

Consider using a wildcard index in the following scenarios:

- If your application queries a collection where field names vary
between documents, create a wildcard index to support queries on all possible document field names.

- If your application repeatedly queries an embedded document field
where the subfields are not consistent, create a wildcard index to support queries on all of the subfields.

- If your application queries documents that share common
characteristics. A compound wildcard index can efficiently cover many queries for documents that have common fields. To learn more, see `wildcard-index-compound`.

## Get Started

You can perform the following tasks with wildcard indexes:

- `create-wildcard-index-single-field`
- `create-wildcard-index-multiple-fields`
- `create-wildcard-index-all-fields`
- `Create a Compound Wildcard Index <create-wildcard-index-compound>`
## Details

Wildcard indexes behave as follows:

- You can create multiple wildcard indexes in a collection.
- A wildcard index can cover the same fields as other indexes in the
collection.

- Wildcard indexes omit the `_id` field by default. To include the
`_id` field in the wildcard index, you must explicitly include it in the `wildcardProjection` document by specifying `{ "_id" : 1 }`.

- Wildcard indexes are `sparse indexes <index-type-sparse>` and
only contain entries for documents that have the indexed field, even if the index field contains a null value.

- Wildcard indexes are distinct from and incompatible with
`wildcard text indexes <create-wildcard-text-index>`. Wildcard indexes cannot support queries using the :query:`$text` operator.

### Covered Queries

Wildcard indexes can support a `covered query <covered-queries>` only if **all** of the following conditions are true:

- The query planner selects the wildcard index to fulfill the query
predicate.

- The query predicate specifies exactly one field covered by the wildcard
index.

- The query projection explicitly excludes `_id` and includes only
the query field.

- The specified query field is never an array.
Consider the following wildcard index on the `employees` collection:

```javascript
db.employees.createIndex( { "$**" : 1 } )
```

The following operation queries for a single field `lastName` and projects out all other fields from the resulting document:

```javascript
db.employees.find(
  { "lastName" : "Doe" },
  { "_id" : 0, "lastName" : 1 }
)
```

If the specified `lastName` is never an array, MongoDB can use the `$**` wildcard index to support a covered query.

## Learn More

To learn more about wildcard indexes, see:

- `wildcard-index-restrictions`
- `wildcard-index-embedded-object-behavior`
- `wildcard-projection-signature`
- `wildcard-index-sort`
## Contents

- Create </core/indexes/index-types/index-wildcard/create-wildcard-index-single-field>
- Include or Exclude Fields </core/indexes/index-types/index-wildcard/create-wildcard-index-multiple-fields>
- Use All Fields </core/indexes/index-types/index-wildcard/create-wildcard-index-all-fields>
- Compound </core/indexes/index-types/index-wildcard/index-wildcard-compound>
- Reference </core/indexes/index-types/index-wildcard/reference>
