---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/rtrim.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $rtrim  (expression operator)

## Definition

## Behavior

- By default, :expression:`$rtrim` removes whitespace,
including the null character, from the end of the input string:

- You can override the default characters to trim using the `chars`
field.

For example, the following trims any `g` and `e` from the end of the input string. Since the input ends with a whitespace, neither character can be trimmed from the end of the string.

- If overriding the default characters to trim, you can explicitly
include the whitespace character(s) to trim in the `chars` field.

For example, the following trims any space or `e` from the end of the input string.

### Whitespace Characters

By default, :expression:`$rtrim` removes the following whitespace, including the null character:

.. include:: /includes/list-table-trim-white-space.rst

## Limitations

.. include:: /includes/fact-trim-chars-length-limit.rst

## Example

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1", quarter: "13Q1", description: " product 1" },
   { _id: 2, item: "ABC2", quarter: "13Q4", description: "product 2 \n The product is in stock.  \n\n  " },
   { _id: 3, item: "XYZ1", quarter: "14Q2", description: null }
] )
```

The following operation uses the :expression:`$rtrim` operator to remove trailing whitespace from the `description` field:

```javascript
db.inventory.aggregate([
   { $project: { item: 1, description: { $rtrim: { input: "$description" } } } }
])
```

The operation returns the following results:

```javascript
{ _id: 1, item: "ABC1", description: " product 1" }
{ _id: 2, item: "ABC2", description: "product 2 \n The product is in stock." }
{ _id: 3, item: "XYZ1", description: null }
```
