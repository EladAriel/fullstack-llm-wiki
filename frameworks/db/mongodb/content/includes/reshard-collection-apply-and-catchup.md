---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reshard-collection-apply-and-catchup.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. versionchanged:: 8.2

During the apply and catch-up phase:

- Each recipient shard begins applying oplog entries that were written
to the the corresponding donor shard after the recipient cloned the data.

- When the estimate for the time remaining to complete the resharding
operation is under **500 ms**, the donor shard blocks writes on the source collection.
