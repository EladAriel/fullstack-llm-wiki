---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-index-key-length-operation-behaviors.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB will **not** create an index on a collection if the index entry for an existing document exceeds the |limit|.

Reindexing operations will error if the index entry for an indexed field exceeds the |limit|. Reindexing operations occur as part of the :dbcommand:`compact` command as well as the :method:`db.collection.reIndex()` method.

Because these operations drop all the indexes from a collection and then recreate them sequentially, the error from the |limit| prevents these operations from rebuilding any remaining indexes for the collection.

MongoDB will not insert into an indexed collection any document with an indexed field whose corresponding index entry would exceed the |limit|, and instead, will return an error. Previous versions of MongoDB would insert but not index such documents.

Updates to the indexed field will error if the updated value causes the index entry to exceed the |limit|.

If an existing document contains an indexed field whose index entry exceeds the limit, any update that results in the relocation of that document on disk will error.

:binary:`~bin.mongorestore` and :binary:`~bin.mongoimport` will not insert documents that contain an indexed field whose corresponding index entry would exceed the |limit|.

In MongoDB 2.6, secondary members of replica sets will continue to replicate documents with an indexed field whose corresponding index entry exceeds the |limit| on initial sync but will print warnings in the logs.

Secondary members also allow index build and rebuild operations on a collection that contains an indexed field whose corresponding index entry exceeds the |limit| but with warnings in the logs.

With mixed version replica sets where the secondaries are version 2.6 and the primary is version 2.4, secondaries will replicate documents inserted or updated on the 2.4 primary, but will print error messages in the log if the documents contain an indexed field whose corresponding index entry exceeds the |limit|.

For existing sharded collections, `chunk migration <sharding-balancing>` will fail if the chunk has a document that contains an indexed field whose index entry exceeds the |limit|.
