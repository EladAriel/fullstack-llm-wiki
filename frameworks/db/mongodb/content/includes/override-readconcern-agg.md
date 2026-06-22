---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/override-readconcern-agg.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To override the default read concern level, use the `readConcern` option. The :dbcommand:`getMore` command uses the `readConcern` level specified in the originating :dbcommand:`aggregate` command.

The following operation on the `movies` collection from the `sample_mflix` database specifies a `read concern <read-concern>` of :readconcern:`"majority"` to read the most recent copy of the data confirmed as having been written to a majority of the nodes.

> **Important:** - .. include:: /includes/fact-aggregate-readConcern.rst
- .. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

.. include:: /includes/usage-read-concern-majority.rst
