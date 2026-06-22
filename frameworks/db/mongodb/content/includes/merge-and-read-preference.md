---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/merge-and-read-preference.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Consider the following points when using :pipeline:`$merge` or :pipeline:`$out` stages in an `aggregation pipeline <aggregation-pipeline>`:

- Starting in MongoDB 5.0, pipelines with a `$merge` stage can run on
replica set `secondary` nodes if all the nodes in the cluster have the `featureCompatibilityVersion <view-fcv>` set to `5.0` or higher and the `read preference <read-preference>` allows secondary reads.

- `$merge` and `$out` stages run on secondary nodes, but write
operations are sent to the `primary` node.

- Not all driver versions support `$merge` operations sent to
the secondary nodes. For details, see the :driver:`driver </>` documentation.

- In earlier MongoDB versions, pipelines with `$out` or `$merge`
stages always run on the primary node and read preference isn't considered.
