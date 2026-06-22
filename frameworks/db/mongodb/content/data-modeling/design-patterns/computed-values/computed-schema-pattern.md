---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/computed-values/computed-schema-pattern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================

# Store Computed Data

An application might need to derive a value from source data stored in a database. Computing a new value can require significant CPU resources, especially in the case of large data sets or in cases where multiple documents must be examined.

If a computed value is requested often, it can be more efficient to save that value in the database ahead of time. When the application requests data, only one read operation is required.

## About this Task

If reads are significantly more common than writes, the computed pattern reduces the frequency of data computation. Instead of computing values on every read, the application stores the computed value and recalculates it as needed. The application can either recompute the value with every write that changes the computed value's source data, or as part of a periodic job.

> **Note:** With periodic updates, the returned computed value is not guaranteed
to be exact. However, this approach may be worth the performance
improvement if exact accuracy isn't a requirement.

## Steps

In this example, an application displays movie viewer and revenue information. Users can look up a particular movie and how much money that movie made.

## Results

The computed pattern reduces CPU workload and increases application performance. Consider the computed pattern your application performs the same calculations repeatedly and has a high read to write ratio.

## Learn More

- `approximation-schema-pattern`
- `schema-pattern-group-data`
- `data-modeling-data-consistency`
