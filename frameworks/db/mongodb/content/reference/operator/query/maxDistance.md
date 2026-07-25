---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/maxDistance.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# $maxDistance (query predicate operator)

## Definition

## Example

The following example query returns documents with location values that are `10` or fewer units from the point `[ -74 , 40 ]`.

```javascript
db.places.find( {
   loc: { $near: [ -74 , 40 ],  $maxDistance: 10 }
} )
```

MongoDB orders the results by their distance from `[ -74 , 40 ]`. The operation returns the first 100 results, unless you modify the query with the :method:`cursor.limit()` method.
