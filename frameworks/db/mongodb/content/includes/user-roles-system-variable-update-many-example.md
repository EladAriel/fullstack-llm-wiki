---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/user-roles-system-variable-update-many-example.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Run:

```javascript
// Attempt to update many documents
db.medical.updateMany(
   // User must have the Provider role to perform the update
   { $expr: { $ne: [ {
      $setIntersection: [ [ "Provider" ], "$$USER_ROLES.role" ] }, []
   ] } },
   // Update diagnosisCode
   { $set: { diagnosisCode: "ACH 02"} }
)
```
