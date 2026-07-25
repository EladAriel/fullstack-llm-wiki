---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/vectorSearch.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================

# $vectorSearch (aggregation stage)

## Definition

## Compatibility

The `$vectorSearch` aggregation pipeline stage is available in the following environments:

- :atlas:`MongoDB Atlas </>` clusters running version 6.0.11 or later
- `MongoDB Enterprise <install-mdb-enterprise>` deployments running version
8.2 or later with the `{+k8s-op-short+} <k8s-operator>`

- `MongoDB Community <install-mdb-community-edition>` deployments running
version 8.2 or later

To learn more, see :atlas:`{+avs+} </atlas-vector-search/vector-search-overview/>`.

## Behavior

Starting in MongoDB 8.0, you can use a `$vectorSearch` stage in a :pipeline:`$unionWith` stage.

## Limitations

You cannot use a `$vectorSearch` stage in a :pipeline:`$facet` stage or a :pipeline:`$lookup` stage.

## Learn More

- To learn more about creating {+avs+} indexes, see
:atlas:`Index Vector Embeddings </atlas-vector-search/vector-search-type/>`.

- To learn more about :pipeline:`$vectorSearch` pipeline stage syntax
and usage, see :atlas:`Vector Search Queries </atlas-vector-search/vector-search-stage/>`.
