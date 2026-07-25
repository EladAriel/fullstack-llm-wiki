---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/searchMeta.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================

# $searchMeta (aggregation stage)

`searchMeta` returns different `types of metadata result <fts-metadata-results>` documents for {+fts+} queries on the field or fields in an Atlas collection. The fields must be covered by a :atlas:`{+fts+} </reference/atlas-search/index-definitions/>` index. See:

- :atlas:`Index Definitions
</reference/atlas-search/index-definitions/>` to learn more about creating and managing {+fts+} indexes.

- :atlas:`{+fts+} Aggregation Pipeline Stages
</reference/atlas-search/query-syntax/>` to learn more about the `$searchMeta` pipeline stage syntax, usage, and results.

> **Important:** The `$searchMeta` aggregation pipeline stage is available for
collections hosted on:
- :atlas:`MongoDB Atlas </>`.
- `MongoDB Enterprise <install-mdb-enterprise>` deployments running
  version 8.2 or later with the `{+k8s-op-short+} <k8s-operator>`.
- `MongoDB Community <install-mdb-community-edition>` deployments
  running version 8.2 or later.
To learn more, see :atlas:`{+fts+} </atlas-search/>`.
