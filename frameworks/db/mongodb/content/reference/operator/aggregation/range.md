---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/range.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

============================

# $range (expression operator)

## Definition

## Behavior

The `<start>` and `<end>` arguments are required and must be integers. The `<non-zero step>` argument is optional, and defaults to `1` if omitted.

## Example

The following example uses a collection called `distances` that lists cities along with their distance in miles from San Francisco.

Documents in the `distances` collection:

```javascript
db.distances.insertMany([
   { _id: 0, city: "San Jose", distance: 42 },
   { _id: 1, city: "Sacramento", distance: 88 },
   { _id: 2, city: "Reno", distance: 218 },
   { _id: 3, city: "Los Angeles", distance: 383 }
]);
```

A bicyclist is planning to ride from San Francisco to each city listed in the collection and wants to stop and rest every 25 miles. The following aggregation pipeline operation uses the `$range` operator to determine the stopping points for each trip.

```javascript
db.distances.aggregate([{
    $project: {
        _id: 0,
        city: 1,
        "Rest stops": { $range: [ 0, "$distance", 25 ] }
    }
}])
```

The operation returns the following:

```javascript
{ "city" : "San Jose", "Rest stops" : [ 0, 25 ] }
{ "city" : "Sacramento", "Rest stops" : [ 0, 25, 50, 75 ] }
{ "city" : "Reno", "Rest stops" : [ 0, 25, 50, 75, 100, 125, 150, 175, 200 ] }
{ "city" : "Los Angeles", "Rest stops" : [ 0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375 ] }
```
