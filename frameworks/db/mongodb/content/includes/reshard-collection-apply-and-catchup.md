---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reshard-collection-apply-and-catchup.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

.. versionchanged:: 8.2

During the apply and catch-up phase:

- Each recipient shard begins applying oplog entries that were written
to the the corresponding donor shard after the recipient cloned the data.

- When the estimate for the time remaining to complete the resharding
operation is under **500 ms**, the donor shard blocks writes on the source collection.
