---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/override-readconcern-agg.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To override the default read concern level, use the `readConcern` option. The :dbcommand:`getMore` command uses the `readConcern` level specified in the originating :dbcommand:`aggregate` command.

The following operation on the `movies` collection from the `sample_mflix` database specifies a `read concern <read-concern>` of :readconcern:`"majority"` to read the most recent copy of the data confirmed as having been written to a majority of the nodes.

> **Important:** - .. include:: /includes/fact-aggregate-readConcern.rst
- .. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

.. include:: /includes/usage-read-concern-majority.rst
