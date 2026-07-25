---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-networkMessageCompressors.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Important:** Messages are compressed when both parties enable network
compression. Otherwise, messages between the parties are
uncompressed.

If you specify multiple compressors, then the order in which you list the compressors matter as well as the communication initiator. For example, if :binary:`~bin.mongosh` specifies the following network compressors `zlib,snappy` and the :binary:`~bin.mongod` specifies `snappy,zlib`, messages between `mongosh` and `mongod` uses `zlib`.

If the parties do not share at least one common compressor, messages between the parties are uncompressed. For example, if `mongosh` specifies the network compressor `zlib` and `mongod` specifies `snappy`, messages between `mongosh` and `mongod` are not compressed.
