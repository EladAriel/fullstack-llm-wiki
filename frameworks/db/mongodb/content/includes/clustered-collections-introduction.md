---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/clustered-collections-introduction.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

|Clustered-collections| store documents in index order rather than the natural order typical of traditional collections. Clustered collections store documents in one `WiredTiger <storage-wiredtiger> file ordered according to the index specification, instead of requiring a separate index file for the default id` index.

Storing the collection's documents in index order can provide benefits for storage and performance compared to traditional collections and their related regular indexes.

Clustered collections are created with a `clustered index <db.createCollection.clusteredIndex>`. The clustered index specifies the order in which documents are stored.

To create a clustered collection, see `clustered-collections-examples`.
