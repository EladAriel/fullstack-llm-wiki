---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/wal-for-extensions.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.436374Z"
---
# Write Ahead Logging for Extensions

  
   Certain extensions, principally extensions that implement custom access
   methods, may need to perform write-ahead logging in order to ensure
   crash-safety. PostgreSQL provides two ways
   for extensions to achieve this goal.
  

  
   First, extensions can choose to use generic
   WAL, a special type of WAL record which describes changes to pages
   in a generic way. This method is simple to implement and does not require
   that an extension library be loaded in order to apply the records. However,
   generic WAL records will be ignored when performing logical decoding.
  

  
   Second, extensions can choose to use a custom
   resource manager. This method is more flexible, supports logical
   decoding, and can sometimes generate much smaller write-ahead log records
   than would be possible with generic WAL. However, it is more complex for an
   extension to implement.
  

&generic-wal;
&custom-rmgr;
