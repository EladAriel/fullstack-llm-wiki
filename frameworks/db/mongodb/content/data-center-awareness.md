---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-center-awareness.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================

# Data Center Awareness

MongoDB provides a number of features that allow application developers and database administrators to customize the behavior of a `sharded cluster` or `replica set` deployment so that MongoDB may be more "data center aware," or allow operational and location-based separation.

MongoDB also supports workload isolation based on functional parameters, to ensure that certain :binary:`~bin.mongod` instances are only used for reporting workloads or that certain high-frequency portions of a sharded collection only exist on specific shards.

The following documents, found either in this section or other sections of this manual, provide information on customizing a deployment for operation- and location-based separation:

`/core/workload-isolation` MongoDB lets you specify that certain application operations use certain :binary:`~bin.mongod` instances.

`/core/zone-sharding` A zone represents one or more ranges of shard key values for a sharded collection. MongoDB routes reads and writes for sharded data covered by a zone only to shards inside that zone. For use in managing data distribution and deployment patterns.

`/tutorial/manage-shard-zone` Administrative tasks related to configuring zones in sharded clusters

## Further Reading

- The `/reference/write-concern` and `/core/read-preference`
documents, which address capabilities related to data center awareness.

- `/tutorial/deploy-geographically-distributed-replica-set`.
## Contents

- Workload Isolation </core/workload-isolation>
