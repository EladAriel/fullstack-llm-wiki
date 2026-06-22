---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-geo-near-returns-sorted-results.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The |geo-operation| operator sorts documents by distance.

- If you use the :method:`~cursor.sort` method in your query,
MongoDB performs a second sort operation, re-ordering the matching documents.  When querying large collections, this can negatively affect query performance.

- If the order of the documents is not important to you, consider
using the :query:`$geoWithin` operator instead, as it returns unsorted results.

- |geo-operation| is a Match Execution operator and is not
permitted in aggregation pipelines.
