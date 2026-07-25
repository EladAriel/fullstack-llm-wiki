---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-distinct-bson-limit-agg-alternative.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** Results must not be larger than the maximum :ref:`BSON size
<limit-bson-document-size>`. If your results exceed the maximum
BSON size, use the aggregation pipeline to retrieve distinct
values using the :pipeline:`$group` operator, as described in
:ref:`Retrieve Distinct Values with the Aggregation Pipeline
<aggregation-group-distinct-values>`.
