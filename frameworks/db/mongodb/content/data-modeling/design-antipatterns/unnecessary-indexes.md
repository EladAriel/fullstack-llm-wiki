---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-antipatterns/unnecessary-indexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# Remove Unnecessary Indexes

Creating indexes for every query can lead to unnecessary indexes, which can degrade database performance. Unnecessary indexes might be rarely used, redundant due to coverage by another compound index, or not used at all. To optimize database performance, it's important to minimize the number of indexes you use. Identify and remove unnecessary indexes to maintain efficient query execution and resource use.

## About this Task

Consider the following `courses` collection, where each document stores information about a different school course.

```javascript
// Biology course document
db.courses.insertOne(
   {
      _id: 1,
      course_name: "Biology 101",
      professor: "Tate",
      semester: "Fall",
      days: "Monday, Friday",
      time: "12:00",
      building: "Olson"
   } 
 )
```

The `courses` collection has an index for every field:

- `_id` is indexed by default
- `{ course_name: 1 }`
- `{ professor: 1 }`
- `{ semester: 1 }`
- `{ building: 1 }`
- `{ days: 1 }`
- `{ time: 1 }`
- `{ day: 1, time: 1 }`
Creating indexes for every field in a collection can lead to bloated collections and negatively impact write performance.

## Steps

## Learn More

- `schema-design-patterns`
- :atlas:`MongoDB Atlas Performance Advisor </performance-advisor>`
- :compass:`Manage Indexes </indexes>`
