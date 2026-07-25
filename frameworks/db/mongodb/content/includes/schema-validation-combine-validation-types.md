---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/schema-validation-combine-validation-types.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For example, consider a `sales` collection with this schema validation:

```javascript
db.createCollection("sales", {
  validator: {
    "$and": [
      // Validation with query operators
      {
        "$expr": {
          "$lt": ["$lineItems.discountedPrice", "$lineItems.price"]
        }
      },
      // Validation with JSON Schema
      {
        "$jsonSchema": {
          "properties": {
            "items": { "bsonType": "array" }
          }
         }
       }
     ]
   }
 }
)
```

The preceding validation enforces these rules for documents in the `sales` collection:

- `lineItems.discountedPrice` must be less than `lineItems.price`.
This rule uses the :expression:`$lt` operator.

- The `items` field must be an array. This rule uses
:query:`$jsonSchema`.
