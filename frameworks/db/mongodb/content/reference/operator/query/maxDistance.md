---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/maxDistance.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
