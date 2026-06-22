---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/clustered-collections-introduction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

|Clustered-collections| store documents in index order rather than the natural order typical of traditional collections. Clustered collections store documents in one `WiredTiger <storage-wiredtiger> file ordered according to the index specification, instead of requiring a separate index file for the default id` index.

Storing the collection's documents in index order can provide benefits for storage and performance compared to traditional collections and their related regular indexes.

Clustered collections are created with a `clustered index <db.createCollection.clusteredIndex>`. The clustered index specifies the order in which documents are stored.

To create a clustered collection, see `clustered-collections-examples`.
