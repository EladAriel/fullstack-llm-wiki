---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/geospatial-places-data-setup.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Create a collection `places` with the following documents:

```javascript
db.places.insertMany( [
   {
      name: "Central Park",
      location: { type: "Point", coordinates: [ -73.97, 40.77 ] },
      category: "Parks"
   },
   {
      name: "Sara D. Roosevelt Park",
      location: { type: "Point", coordinates: [ -73.9928, 40.7193 ] },
      category: "Parks"
   },
   {
      name: "Polo Grounds",
      location: { type: "Point", coordinates: [ -73.9375, 40.8303 ] },
      category: "Stadiums"
   }
] )
```

The following operation creates a `2dsphere` index on the `location` field:

```javascript
db.places.createIndex( { location: "2dsphere" } )
```
