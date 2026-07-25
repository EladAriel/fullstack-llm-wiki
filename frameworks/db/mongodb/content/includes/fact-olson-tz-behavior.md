---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-olson-tz-behavior.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When using an Olson Timezone Identifier in the `<timezone>` field, MongoDB applies the :abbr:`DST (Daylight Savings Time)` offset if applicable for the specified timezone.

For example, consider a `sales` collection with the following document:

```javascript
db.sales.insertOne(
 {
  "_id" : 1,
  "item" : "abc",
  "price" : 10,
  "quantity" : 2,
  "date" : ISODate("2014-01-01T08:15:39.736Z")
 } 
)
```

The following aggregation illustrates how MongoDB handles the DST offset for the Olson Timezone Identifier. The example uses the :expression:`$hour` and :expression:`$minute` operators to return the corresponding portions of the `date` field:

```javascript
db.sales.aggregate([
{
   $project: { 
      "nycHour": { 
         $hour: { date: "$date", timezone: "-05:00" }
       }, 
       "nycMinute": { 
          $minute: { date: "$date", timezone: "-05:00" }
       },
       "gmtHour": {
          $hour: { date: "$date", timezone: "GMT" }
       },
       "gmtMinute": {
          $minute: { date: "$date", timezone: "GMT" } },
       "nycOlsonHour": {
          $hour: { date: "$date", timezone: "America/New_York" }
       },
       "nycOlsonMinute": {
          $minute: { date: "$date", timezone: "America/New_York" }
       }
   }
}])
```

The operation returns the following result:

```javascript
{
   "_id": 1,
   "nycHour" : 5,
   "nycMinute" : 24,
   "gmtHour" : 10,
   "gmtMinute" : 24,
   "nycOlsonHour" : 6,
   "nycOlsonMinute" : 24
}
```
