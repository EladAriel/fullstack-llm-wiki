---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/example-qe-csfle-contention.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
