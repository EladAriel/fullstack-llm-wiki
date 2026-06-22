---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/example-setup-01.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
