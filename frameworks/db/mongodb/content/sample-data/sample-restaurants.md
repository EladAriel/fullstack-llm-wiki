---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/sample-data/sample-restaurants.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# Sample Restaurants Dataset

The `sample_restaurants` database contains two collections specifically designed to help familiarize you with :manual:`GeoJSON </reference/geojson/>` data.

.. include:: /includes/search-shared/fact-how-to-load-sample-data.rst

## Collections

The `sample_restaurants` database contains the following collections:

### `sample_restaurants.restaurants`

This collection contains account details for restaurants. Each document contains details on the restaurant such as its address, borough, review scores, its name, and the type of food it serves.

Indexes ```````

The `sample_restaurants.restaurants` collection contains the following indexes:

Sample Document ```````````````

```json
{
 "address": {
   "building": "8825",
   "coord": [-73.8803827, 40.7643124],
   "street": "Astoria Boulevard",
   "zipcode": "11369"
 },
 "borough": "Queens",
 "cuisine": "American",
 "grades": [ {
   "date": {"$date": "2014-11-15T00:00:00.000Z"},
   "grade": "Z",
   "score": 38
 },
 {
   "date": {"$date": "2014-05-02T00:00:00.000Z"},
   "grade": "A",
   "score": 10
 },
 {
   "date": {"$date": "2013-03-02T00:00:00.000Z"},
   "grade": "A",
   "score": 7
 },
 {
   "date": {"$date": "2012-02-10T00:00:00.000Z"},
   "grade": "A",
   "score": 13
 }],
   "name": "Brunos On The Boulevard",
   "restaurant_id": "40356151"
}
```

### `sample_restaurants.neighborhoods`

This collection contains details on the various neighborhoods of New York City neighborhoods. Each document contains the name of the neighborhood, and a geometry sub-document which contains the shape of the neighborhood.

These arrays of coordinates are typically used with the :query:`$geoWithin` operator to query data that exists within a specified boundary.

Indexes ```````

The `sample_restaurants.neighborhoods` collection contains the following indexes:

Sample Document ```````````````

```json
{
 "geometry": {
   "coordinates": [[
     [-73.94193078816193, 40.70072523469547],
     [-73.9443878859649, 40.70042452378256],
     [-73.94424286147482, 40.69969927964773],
     [-73.94409591260093, 40.69897295461309],
     [-73.94394947271304, 40.69822127983908],
     ...
     [-73.94193078816193, 40.70072523469547]
   ]]},
 "name":"Bedford"
}
```
