---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-antipatterns/reduce-collections.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# Reduce the Number of Collections

Creating too many collections can decrease performance. With every collection, MongoDB creates a default `_id index <indexes>`, which uses additional storage. If you create excessive collections, those collections and indexes can strain replica set resources and decrease performance.

## About this Task

Consider the following schema that stores daily temperature readings that are taken every hour. The `temperature` database stores each day's readings in separate collections.

```javascript
// Temperatures for May 10, 2024
{
   _id: 1,
   timestamp: "2024-05-10T010:00:00Z",
   temperature: 60
},
{
   _id: 2
   timestamp: "2024-05-10T011:00:00Z",
   temperature: 61
},
{
   _id: 3
   timestamp: "2024-05-10T012:00:00Z",
   temperature: 64
}
...
```

```javascript
// Temperatures for May 11, 2024
{
   _id: 1,
   timestamp: "2024-05-11T010:00:00Z",
   temperature: 68
},
{
   _id: 2
   timestamp: "2024-05-11T011:00:00Z",
   temperature: 72
},
{
   _id: 3
   timestamp: "2024-05-11T012:00:00Z",
   temperature: 72
}
...
```

With an unbound number of collections, the number of default `_id` indexes can grow to degrade performance.

Additionally, this approach requires a :pipeline:`$lookup` operation to query across multiple collections. `$lookup` operations add query complexity and can strain resources.

To reduce the number of collections, drop or archive unused collections, or remodel your data schema by consolidating related collections, denormalizing data, or leveraging embedded documents where appropriate.

## Example

You can modify the schema to store each day's temperature readings in a single collection. For example:

```javascript
db.dailyTemperatures.insertMany( [
   {
      _id: ISODate("2024-05-10T00:00:00Z"),
      readings: [
         {
            timestamp: "2024-05-10T10:00:00Z",
            temperature: 60
         },
         {
            timestamp: "2024-05-10T11:00:00Z",
            temperature: 61
         },
         {
            timestamp: "2024-05-10T12:00:00Z",
            temperature: 64
         }
      ]
   },
   {
      _id: ISODate("2024-05-11T00:00:00Z"),
      readings: [
         {
            timestamp: "2024-05-11T10:00:00Z",
            temperature: 68
         },
         {
            timestamp: "2024-05-11T11:00:00Z",
            temperature: 72
         },
         {
            timestamp: "2024-05-11T12:00:00Z",
            temperature: 72
         }
      ]
   }
] )
```

The updated schema requires fewer resources than the original. Instead of needing a separate index for each day, the default `_id` index now facilitates queries by date.

## Learn More

- `schema-design-antipatterns`
- `schema-design-patterns`
