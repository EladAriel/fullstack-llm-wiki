---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-encryptedFieldsConfig-intro.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To use encrypted fields in a collection, specify a new configuration option. You must have permissions to create and modify a collection to set this configuration during collection creation. After you create a collection, the `encryptedFields` value is immutable.

The configuration includes a list of fields and their corresponding key identifiers, types, and supported queries.

```javascript
encryptedFieldsConfig = {
    "fields": [
      {
        "keyId": UUID,                    // required
        "path": String,                   // path to field, required
        "bsonType": "string" | "int" ..., // required
        "queries":                        // optional
        [ 
          { "queryType": "equality" },
        ]
      }
    ]
}
```
