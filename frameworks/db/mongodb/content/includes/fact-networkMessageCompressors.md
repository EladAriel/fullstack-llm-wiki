---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-networkMessageCompressors.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** Messages are compressed when both parties enable network
compression. Otherwise, messages between the parties are
uncompressed.

If you specify multiple compressors, then the order in which you list the compressors matter as well as the communication initiator. For example, if :binary:`~bin.mongosh` specifies the following network compressors `zlib,snappy` and the :binary:`~bin.mongod` specifies `snappy,zlib`, messages between :binary:`~bin.mongosh` and :binary:`~bin.mongod` uses `zlib`.

If the parties do not share at least one common compressor, messages between the parties are uncompressed. For example, if :binary:`~bin.mongosh` specifies the network compressor `zlib` and :binary:`~bin.mongod` specifies `snappy`, messages between :binary:`~bin.mongosh` and :binary:`~bin.mongod` are not compressed.
