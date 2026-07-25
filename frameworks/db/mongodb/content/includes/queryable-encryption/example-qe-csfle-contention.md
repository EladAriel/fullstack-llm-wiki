---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/example-qe-csfle-contention.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The example below sets `contention` to 0 for the low cardinality Social Security Number (SSN) and patient ID fields, since these are unique identifiers that shouldn't repeat in the data set.

```javascript
const encryptedFieldsObject = {
   fields: [
      {
         path: "patientId",
         bsonType: "int",
         queries: { queryType: "equality",
                    contention: "8"}
      },
      {
         path: "patientInfo.ssn",
         bsonType: "string",
         queries: { queryType: "equality",
                    contention: "8"}
      },
      {
         path: "medications",
         bsonType: "array"
      },
      {
         path: "patientInfo.billing",
         bsonType: "object"
      }
   ]
}
```
