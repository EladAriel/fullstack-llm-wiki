---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/validate-improvements-introduction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 6.2, the :dbcommand:`validate` command and :method:`db.collection.validate()` method:

- Check collections to ensure the
`BSON documents <bson-document-format>` conform to the BSON specifications.

- Check `time series collections <manual-timeseries-collection>`
for internal data inconsistencies.

- Have a new option `checkBSONConformance` that enables comprehensive
BSON checks.

Starting in MongoDB 8.3, the `validate` command and `db.collection.validate()` method check collections to ensure a collection doesn't have any documents that exceed 16 MB.
