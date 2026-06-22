---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/mongot-sizing/advanced-guidance/resource-allocation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================================

# Resource Allocation Considerations for mongot Deployments

This section answers critical planning questions about your `mongot` deployment and provides actionable steps to design your search architecture. For a comprehensive overview, read this section linearly. Alternatively, you can use this section as a reference, skipping to relevant sections as needed. The goal of this section is to help accurately estimate resource requirements and build a robust deployment.

## Data Characteristics and Indexes

Your data's structure and index definition are the primary drivers of **disk usage** and **RAM requirements**. Use this section to estimate the final index size and the memory needed to manage indexes efficiently.

## Indexing Workload

The rate and type of your writes (inserts, updates, deletes) determine the **CPU** and **Disk IOPS** needed to keep your search index synchronized with your database.

To provision for write throughput and maintenance:

## Query Workload

Query performance is primarily a function of CPU for processing and RAM for caching. The complexity and volume of your queries determine the resources needed to meet your latency targets.

To estimate required deployment sizes for query performance:
