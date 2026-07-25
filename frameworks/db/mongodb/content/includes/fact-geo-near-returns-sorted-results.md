---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-geo-near-returns-sorted-results.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The |geo-operation| operator sorts documents by distance.

- If you use the :method:`~cursor.sort` method in your query,
MongoDB performs a second sort operation, re-ordering the matching documents.  When querying large collections, this can negatively affect query performance.

- If the order of the documents is not important to you, consider
using the :query:`$geoWithin` operator instead, as it returns unsorted results.

- |geo-operation| is a Match Execution operator and is not
permitted in aggregation pipelines.
