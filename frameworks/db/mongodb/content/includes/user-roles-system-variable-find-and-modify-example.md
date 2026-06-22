---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/user-roles-system-variable-find-and-modify-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Run:

```javascript
// Attempt to find and modify document
db.medical.findAndModify( {
   query:
      { $and: [
         {
            // Only update the document for Mary Smith
            patientName: { $eq: "Mary Smith" }
         },
         {
            // User must have the Provider role to perform the update
            $expr: { $ne: [ {
               $setIntersection: [ [ "Provider" ], "$$USER_ROLES.role" ]
            }, [] ] }
         }
      ]
   },
   // Update document
   update: {
      patientName: "Mary Smith",
      diagnosisCode: "ACH 03",
      creditCard: "6541-7534-9637-3456"
   }
} )
```
