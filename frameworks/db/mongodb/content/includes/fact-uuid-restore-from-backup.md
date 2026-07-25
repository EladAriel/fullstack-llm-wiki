---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-uuid-restore-from-backup.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
