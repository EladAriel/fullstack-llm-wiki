---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/trim.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $trim  (expression operator)

## Definition

## Behavior

- By default, :expression:`$trim` removes whitespace characters,
including the null character:

- You can override the default characters to trim using the `chars`
field.

For example, the following trims any `g` and `e` from the start and end of the input. Since the input starts with a whitespace, neither character can be trimmed from the start of the string.

- If overriding the default characters to trim, you can explicitly
include the whitespace character(s) to trim in the `chars` field.

For example, the following trims any space, `g`, `e` from the start and end of the input.

### Whitespace Characters

By default, :expression:`$trim` removes the following whitespaces, including the null character:

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

The following operation uses the :expression:`$trim` operator to remove leading and trailing whitespaces from the `description` field:

```javascript
db.inventory.aggregate([
   { $project: { item: 1, description: { $trim: { input: "$description" } } } }
])
```

The operation returns the following results:

```javascript
{ _id: 1, item: "ABC1", description: "product 1" }
{ _id: 3, item: "XYZ1", description: null }
{ _id: 2, item: "ABC2", description: "product 2 \n The product is in stock." }
```
