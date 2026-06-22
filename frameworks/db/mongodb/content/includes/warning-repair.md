---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-repair.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** - Only use :option:`mongod --repair` if you have no other options.
  The operation removes and does not save any corrupt data during
  the repair process.
- Avoid running :option:`--repair <mongod --repair>` against
  a replica set member:
  - To repair a `replica set` member, if you have an intact
    copy of your data available (e.g. a recent backup or an intact
    member of the `replica set`), restore from that intact
    copy instead. To learn more, see `resync-replica-member`.
  - If you choose to run :option:`mongod --repair` against a
    replica set member and the operation modifies the data or the
    metadata, you must still perform a full resync in order for the
    member to rejoin the replica set.
- Before using :option:`--repair <mongod --repair>`, make a backup
  copy of the :option:`dbpath <mongod --dbpath>` directory.
- If repair fails to complete for any reason, you must restart the
  instance using the :option:`--repair <mongod --repair>` option.
