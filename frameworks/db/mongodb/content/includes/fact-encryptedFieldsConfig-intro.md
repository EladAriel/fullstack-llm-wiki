---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-encryptedFieldsConfig-intro.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
