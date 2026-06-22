---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/dot-dollar-considerations/periods.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Field Names with Periods

This section summarizes how to insert, query, and update documents with field names that contain a period. MongoDB discourages the use of field names that contain a period because some features aren't supported with these fields. See `dot-dollar-general-restrictions` for more information.

> **Note:** Limit the number of words separated by periods in field names to less
than 255. If you attempt to use more, MongoDB returns an error.

## Insert a Field Name with a Period

To insert a document that contains a field name with a period, put the field name in quotes.

The following command inserts a document that contains a field name `price.usd`:

```javascript
db.inventory.insertOne(
   { 
      "item" : "sweatshirt", 
      "price.usd": 45.99,
      "quantity": 20
   }
)
```

## Query a Field that has a Period

To query for a field that has a period, use the :expression:`$getField` operator.

The following query returns documents where the `price.usd` field is greater than `40`:

If you don't use `$getField`, MongoDB treats the field name with a period as an embedded object. For example, the following query matches documents where a `usd` field inside of a `price` field is greater than `40`:

```javascript
db.inventory.find( {
   "price.usd": { $gt: 40 }
} )
```

The preceding query would match this document:

```javascript
{ 
   "item" : "sweatshirt", 
   "price": {
      "usd": 45.99
   },
   "quantity": 20
}
```

## Update a Field that has a Period

To update a field that has a period, use an aggregation pipeline with the :expression:`$setField` operator.

The following operation sets the `price.usd` field to `29.99`:

```javascript
db.inventory.updateOne(
   { "item": "sweatshirt" },
   [
      { 
         $replaceWith: {
            $setField: {
               field: "price.usd",
               input: "$$ROOT",
               value: 29.99
            }
         }
      }
   ]
)
```

If you don't use `$setField`, MongoDB treats the field name with a period as an embedded object. For example, the following operation does not update the existing `price.usd` field, and instead inserts a new field `usd`, embedded inside of a `price` field:

```javascript
db.inventory.updateOne(
   { "item": "sweatshirt" },
   { $set: { "price.usd": 29.99 } }
)
```

Resulting document:

```javascript
[
   {
      _id: ObjectId("66145f9bcb1d4abffd2f1b50"),
      item: 'sweatshirt',
      'price.usd': 45.99
      quantity: 20,
      price: { usd: 29.99 }
   }
]
```

For more examples of updates with aggregation pipelines, see `updates-agg-pipeline`.

## Learn More

- :expression:`$getField`
- :expression:`$setField`
- :expression:`$literal`
- `dollar-prefix-field-names`
