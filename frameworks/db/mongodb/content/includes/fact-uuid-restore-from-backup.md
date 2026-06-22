---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-uuid-restore-from-backup.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. note :

```
All MongoDB collections have
:abbr:`UUIDs (Universally unique identifiers)` by default. When
MongoDB restores collections, the restored collections retain their
original UUIDs. When restoring a collection where no UUID was
present, MongoDB generates a UUID for the restored collection. 

For more information on collection UUIDs, see :ref:`<collections>`.
```
