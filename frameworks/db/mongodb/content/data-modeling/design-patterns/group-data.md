---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/group-data.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========

# Group Data

If your schema contains a large series of data, grouping that data into multiple smaller series can improve performance.

Your schema may also need to handle outliers in a series that cause poor performance for more common data values. To improve performance and organization for groups of data, you can use the `bucket <group-data-bucket-pattern>` and `outlier <group-data-outlier-pattern>` patterns.

## Use Cases

> **Tip:** `Time series collections <manual-timeseries-collection>` apply
the bucket pattern automatically, and are suitable for most use cases
of the bucket pattern.

## Get Started

To learn how to apply design patterns to group data, see these pages:

- `group-data-bucket-pattern`
- `group-data-outlier-pattern`
## Learn More

- `data-modeling-schema-design`
- `schema-design-patterns`
- `timeseries-create-query-procedures`
## Contents

- Bucket Pattern </data-modeling/design-patterns/group-data/bucket-pattern>
- Outlier Pattern </data-modeling/design-patterns/group-data/outlier-pattern>
- Attribute Pattern </data-modeling/design-patterns/group-data/attribute-pattern>
- Subset Pattern </data-modeling/design-patterns/group-data/subset-pattern>
