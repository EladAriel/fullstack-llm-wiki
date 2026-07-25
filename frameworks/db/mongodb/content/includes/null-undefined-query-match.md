---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/null-undefined-query-match.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.0, comparisons to `null` in equality match expressions don't match `undefined` values.

For example, consider these documents and query:

```javascript
// create the people collection

db.people.insertMany( [
   { _id: 1, name: null },
   { _id: 2, name: undefined },
   { _id: 3, name: [ "Gabriel", undefined ] },
   { _id: 4, names: [ "Alice", "Charu" ] }
] )
```

```javascript
db.people.find( { name: null } )
```

Prior to MongoDB 8.0, the preceding query would match documents where:

- The `name` field is `null (id: 1`)
- The `name` field is `undefined` or contains an `undefined` array
element (`_id: 2 and id: 3`)

- The `name field does not exist (id: 4`)
Starting in MongoDB 8.0, the preceding query does not match documents where the `name` field is `undefined` or contains `undefined` array elements. The query only matches documents where:

- The `name` field is `null` or contains a `null` array element
(`_id: 1`)

- The `name field does not exist (id: 4`)
This query behavior change also impacts these operations:

- :query:`$eq`
- :query:`$in`
- :pipeline:`$lookup`, because a `null` local field no longer matches
an `undefined` foreign field.
