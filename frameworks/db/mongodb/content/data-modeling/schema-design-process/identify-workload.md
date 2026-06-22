---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/schema-design-process/identify-workload.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# Identify Application Workload

The first step in the `schema design process <data-modeling-schema-design>` is to identify the operations that your application runs most frequently. This helps you create effective indexes and minimize the number of calls the application makes to the database.

Consider the scenarios your application currently supports and scenarios it may support in the future.

## Steps

## Example

The following example shows a workload table for a blog application:

## Next Steps

After you identify your application's workload, the next step in the schema design process is to map related data in your schema. See `data-modeling-map-relationships`.
