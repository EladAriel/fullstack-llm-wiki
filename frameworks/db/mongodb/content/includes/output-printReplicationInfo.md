---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/output-printReplicationInfo.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

## Output Example

The following example is a sample output from the |method| method run on the primary:

```none
configured oplog size:   192MB
log length start to end: 65422secs (18.17hrs)
oplog first event time:  Mon Jun 23 2014 17:47:18 GMT-0400 (EDT)
oplog last event time:   Tue Jun 24 2014 11:57:40 GMT-0400 (EDT)
now:                     Thu Jun 26 2014 14:24:39 GMT-0400 (EDT)
```

## Output Fields

|method| formats and prints the data returned by :method:`db.getReplicationInfo()`:

configured oplog size Displays the `db.getReplicationInfo().logSizeMB` value.

log length start to end Displays the `db.getReplicationInfo().timeDiff` and `db.getReplicationInfo().timeDiffHours` values.

oplog first event time Displays the `db.getReplicationInfo().tFirst`.

oplog last event time Displays the `db.getReplicationInfo().tLast`.

now Displays the `db.getReplicationInfo().now`.

See :method:`db.getReplicationInfo()` for description of the data.
