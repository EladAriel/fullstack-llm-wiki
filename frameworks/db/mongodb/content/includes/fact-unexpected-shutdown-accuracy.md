---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-unexpected-shutdown-accuracy.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

After an unclean shutdown of a :binary:`~bin.mongod` using the `Wired Tiger </core/wiredtiger>` storage engine, |opt| statistics reported by |cmd| may be inaccurate.

The amount of drift depends on the number of insert, update, or delete operations performed between the last `checkpoint <storage-wiredtiger-checkpoints>` and the unclean shutdown. Checkpoints usually occur every 60 seconds. However, :binary:`~bin.mongod` instances running with non-default :option:`--syncdelay <mongod --syncdelay>` settings may have more or less frequent checkpoints.

Run :dbcommand:`validate` on each collection on the :binary:`~bin.mongod` to restore statistics after an unclean shutdown.

After an unclean shutdown:

- :dbcommand:`validate` updates the :ref:`count statistic
<collstat-count>` in the :dbcommand:`collStats` `output <collStats-output>` with the latest value.

- Other statistics like the number of documents inserted or removed in
the :dbcommand:`collStats` `output <collStats-output>` are estimates.
