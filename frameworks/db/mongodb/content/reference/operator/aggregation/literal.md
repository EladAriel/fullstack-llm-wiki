---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/literal.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $literal (expression operator)

## Definition

## Behavior

If the `<value>` is an `expression <aggregation-expressions>`, :expression:`$literal` does not evaluate the expression but instead returns the unparsed expression.

## Examples

### Treat `$` as a Literal

In `expression <aggregation-expressions>`, the dollar sign `$` evaluates to a field path; i.e. provides access to the field. For example, the :expression:`$eq` expression `$eq: [ "$price", "$1" ]` performs an equality check between the value in the field named `price` and the value in the field named `1` in the document.

The following example uses a :expression:`$literal` expression to treat a string that contains a dollar sign `"$1"` as a constant value.

A `storeInventory` collection has the following documents:

```javascript
db.storeInventory.insertMany( [
   { "_id" : 1, "item" : "napkins", price: "$2.50" },
   { "_id" : 2, "item" : "coffee", price: "1" },
   { "_id" : 3, "item" : "soap", price: "$1" }
] )
```

```javascript
db.storeInventory.aggregate( [
   { $project: { costsOneDollar: { $eq: [ "$price", { $literal: "$1" } ] } } }
] )
```

This operation projects a field named `costsOneDollar` that holds a boolean value, indicating whether the value of the `price` field is equal to the string `"$1"`:

```javascript
{ "_id" : 1, "costsOneDollar" : false }
{ "_id" : 2, "costsOneDollar" : false }
{ "_id" : 3, "costsOneDollar" : true }
```

### Project a New Field with Value `1`

The :pipeline:`$project` stage uses the expression `<field>: 1` to include the `<field>` in the output. The following example uses the :expression:`$literal` to return a new field set to the value of `1`.

A `books` collection has the following documents:

```javascript
db.books.insertMany([
   { "_id" : 1, "title" : "Dracula", "condition": "new" },
   { "_id" : 2, "title" : "The Little Prince", "condition": "new" }
])
```

The :expression:`{ $literal: 1 } <$literal>` expression returns a new `editionNumber` field set to the value `1`:

```javascript
db.books.aggregate( [
   { $project: { "title": 1, "editionNumber": { $literal: 1 } } }
] )
```

The operation results in the following documents:

```javascript
{ "_id" : 1, "title" : "Dracula", "editionNumber" : 1 }
{ "_id" : 2, "title" : "The Little Prince", "editionNumber" : 1 }
```
