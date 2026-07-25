---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/people-collection.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Create a sample collection named `people` with these documents:

```javascript
db.people.insertMany( [
   { _id: 1, name: "Melissa", hobbies: [ "softball", "drawing", "reading" ] },
   { _id: 2, name: "Brad", hobbies: [ "gaming", "skateboarding" ] },
   { _id: 3, name: "Scott", hobbies: [ "basketball", "music", "fishing" ] },
   { _id: 4, name: "Tracey", hobbies: [ "acting", "yoga" ] },
   { _id: 5, name: "Josh", hobbies: [ "programming" ] },
   { _id: 6, name: "Claire" }
] )
```

The `hobbies` field contains an array of each person's hobbies in ranked order. The first hobby in the array is the person's primary hobby that the person spends the most time on. The first hobby has an array index of `0`.
