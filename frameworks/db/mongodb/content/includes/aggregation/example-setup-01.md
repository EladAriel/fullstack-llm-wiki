---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/example-setup-01.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The following examples use the `testScores` collection. Create the collection:

```javascript
db.testScores.insertMany( [
   { studentId: "2345", test01: 62, test02: 81, test03: 80 },
   { studentId: "2356", test01: 60, test02: 83, test03: 79 },
   { studentId: "2358", test01: 67, test02: 82, test03: 78 },
   { studentId: "2367", test01: 64, test02: 72, test03: 77 },
   { studentId: "2369", test01: 60, test02: 53, test03: 72 }
] )
```
