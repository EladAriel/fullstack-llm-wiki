---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-document-duplicate-key-names-body.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The MongoDB Query Language doesn't support documents with duplicate field names:

- Although some BSON builders may support creating a BSON document with
duplicate field names, inserting these documents into MongoDB isn't supported even if the insert succeeds, or appears to succeed.

- For example, inserting a BSON document with duplicate field names
through a MongoDB driver may result in the driver silently dropping the duplicate values prior to insertion, or may result in an invalid document being inserted that contains duplicate fields. Querying those documents leads to inconsistent results.

- Updating documents with duplicate field names isn't
supported, even if the update succeeds or appears to succeed.

Starting in MongoDB 6.1, to see if a document has duplicate field names, use the :dbcommand:`validate` command with the `full` field set to `true`. In any MongoDB version, use the :expression:`$objectToArray` aggregation operator to see if a document has duplicate field names.
