---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-ttl-collection-background-timing.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The TTL index does not guarantee that expired data is deleted immediately upon expiration. There may be a delay between the time that a document expires and the time that MongoDB removes the document from the database.

The background task that removes expired documents runs every 60 seconds. As a result, documents may remain in a collection during the period between the expiration of the document and the running of the background task. MongoDB starts deleting documents 0 to 60 seconds after the index completes.

Because the duration of the removal operation depends on the workload of your :binary:`~bin.mongod` instance, expired data may exist for some time beyond the 60 second period between runs of the background task.

The delete operations initiated by the TTL task run in the foreground, like other deletes.
