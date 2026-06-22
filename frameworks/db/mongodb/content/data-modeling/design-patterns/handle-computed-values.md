---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/handle-computed-values.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# Handle Computed Values

If you want to return calculated data values to your application, you can improve performance by running computations in your database rather than when the data is requested. The application may require either precise calculations or approximate results. By using the `Computed <computed-schema-pattern>` and the `Approximation <approximation-schema-pattern>` schema patterns, you can pre-compute and store the resulting values ahead of time (for example on insert or with a periodic task) so they are readily available when you request the data.

## Use Cases

## Get Started

To learn how to apply design patterns for computed values, see these pages:

- `computed-schema-pattern`
- `approximation-schema-pattern`
## Learn More

- `data-modeling-schema-design`
- `schema-design-patterns`
## Contents

- Computed Data </data-modeling/design-patterns/computed-values/computed-schema-pattern>
- Approximation Pattern </data-modeling/design-patterns/computed-values/approximation-schema-pattern>
