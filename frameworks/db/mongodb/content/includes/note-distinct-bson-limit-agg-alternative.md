---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-distinct-bson-limit-agg-alternative.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:** Results must not be larger than the maximum :ref:`BSON size
<limit-bson-document-size>`. If your results exceed the maximum
BSON size, use the aggregation pipeline to retrieve distinct
values using the :pipeline:`$group` operator, as described in
:ref:`Retrieve Distinct Values with the Aggregation Pipeline
<aggregation-group-distinct-values>`.
