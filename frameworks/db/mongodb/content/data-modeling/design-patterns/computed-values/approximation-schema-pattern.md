---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/computed-values/approximation-schema-pattern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# Use the Approximation Pattern

Use the approximation pattern when you have values that change frequently, but users don't need to know precise values. Instead of updating values every time data changes, the approximation pattern updates data based on a larger granularity, which results in fewer updates and a lower application workload.

## About this Task

The approximation pattern is useful when values don't need to be reported exactly. For example:

- City population
- Website visits
- Airline travelers
The preceding measurements are typically useful when approximated. The application can save time and resources by updating stored values by hundreds or thousands, depending on the scale of the data.

## Steps

In this example, an application displays population data for a city of roughly 40,000 people. Application users are primarily looking for overall trends and don't need to know the exact city population.

## Results

The preceding application logic might result in these documents:

```javascript
db.population.insertMany( [
   {
      city: "New Perth",
      population: 40100,
      date: ISODate("2024-09-20")
   },
   {
      city: "New Perth",
      population: 40200,
      date: ISODate("2024-10-01")
   },
   {
      city: "New Perth",
      population: 40300,
      date: ISODate("2024-10-09")
   },
] )
```

> **Note:** How the updated values are gathered depends on your scenario.
In this example, updated population values can be gathered from
census reports.

By updating the population with a granularity of 100, the approximation pattern reduces the number of updates to 1% of the updates that would be required to track individual population changes.

Users can see the population increasing over time, which meets their needs of seeing high-level trends.

## Learn More

- `computed-schema-pattern`
- `data-modeling-data-consistency`
- `schema-pattern-group-data`
