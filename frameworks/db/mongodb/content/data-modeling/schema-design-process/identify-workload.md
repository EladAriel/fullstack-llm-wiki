---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/schema-design-process/identify-workload.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
