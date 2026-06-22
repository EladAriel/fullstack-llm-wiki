---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/recover-data-following-unexpected-shutdown.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================================

# Recover a Self-Managed Standalone after Unexpected Shutdown

> **Warning:** The following procedure applies to standalone :binary:`~bin.mongod`
instance version {+version+}. For other MongoDB versions, refer to
the corresponding version of the manual.
Do not use this tutorial to recover a member of a :term:`replica
set`. Instead, you should either restore from a :doc:`backup
</core/backups>` or resync from another member of the set, as
described in `/tutorial/resync-replica-set-member`.

> **Tip:** .. include:: /includes/note-repair.rst

Disk-level data corruption or missing data files can prevent :binary:`~bin.mongod` instance from starting, and journal files may be insufficient to recover automatically:

```none
2018-10-24T18:05:18.248-04:00 W STORAGE  [initandlisten] Detected unclean shutdown - mongod.lock is not empty.

...

2018-10-24T17:24:53.122-04:00 E STORAGE  [initandlisten] Failed to get the cursor for uri: table:collection-2-6854866147293273505
2018-10-24T17:24:53.122-04:00 E STORAGE  [initandlisten] This may be due to missing data files. ...

...

***aborting after fassert() failure
```

In such cases, your :setting:`~storage.dbPath` contains a non-empty :file:`mongod.lock` file.

The following procedure uses :option:`mongod --repair` to recover from these cases:

> **Warning:** Only use :option:`mongod --repair` if you have no other options.
The operation removes and does not save any corrupt data during the
repair process.

For the WiredTiger storage engine, :option:`mongod --repair`:

- Rebuilds all indexes for collections with one or more inconsistent
indexes.

- Discards corrupt data.
- Creates empty/stub files for missing data/metadata files.
## Procedure

> **Important:** Run the repair operation as the same user that normally runs the
:binary:`~bin.mongod` process to avoid changing the permissions of the
MongoDB data files.

.. include:: /includes/steps/recover-data-with-repairpath.rst

> **Note:** If the repair fails to complete for any reason, you
must restart the instance with the :option:`--repair <mongod
--repair>` option to complete the repair.

Generally, you should not manually remove the `mongod.lock` file. Instead, use the above procedure to recover the database. In dire situations, you can remove the file, start the database using the possibly corrupt files, and attempt to recover data from the database. However, it is impossible to predict the state of the database in these situations.
