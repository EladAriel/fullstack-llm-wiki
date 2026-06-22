---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/project-fields-from-query-results.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/java-sync-links.rst

.. include:: /includes/java-async-links.rst

===================================

# Project Fields to Return from Query

Use projection to select which document fields a query returns. You can use the following methods:

.. include:: /includes/fact-methods.rst

By default, queries in MongoDB return all fields in matching documents. To limit the amount of data that MongoDB sends to applications, you can include a `projection` document to specify or restrict fields to return.

## Additional Considerations

- .. |$project| replace:: :pipeline:`$project` aggregation
.. include:: /includes/aggregation/fact-project-stage-placement.rst

- MongoDB enforces additional restrictions with regards to projections.
See :limit:`Projection Restrictions` for details.

> **Seealso:** - `find-projection`
- `/tutorial/query-documents`
