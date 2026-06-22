---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-replica-set-secondary-sync-target.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================================

# Configure a Self-Managed Secondary's Sync Target

## Overview

Secondaries capture data from the primary member to maintain an up to date copy of the sets' data. However, by default secondaries may automatically change their sync targets to secondary members based on changes in the ping time between members and the state of other members' replication. See `/core/replica-set-sync` and `chained-replication` for more information.

For some deployments, implementing a custom replication sync topology may be more effective than the default sync target selection logic. MongoDB provides the ability to specify a host to use as a sync target.

To temporarily override the default sync target selection logic, you may manually configure a `secondary` member's sync target to temporarily pull `oplog` entries. The following provide access to this functionality:

- :dbcommand:`replSetSyncFrom` command, or
- :method:`rs.syncFrom()` helper in :binary:`~bin.mongosh`
## Considerations

.. include:: /includes/extracts/rsSyncFrom-behavior-both.rst

## Procedure

To use the :dbcommand:`replSetSyncFrom` command in :binary:`~bin.mongosh`:

```javascript
db.adminCommand( { replSetSyncFrom: "hostname<:port>" } );
```

To use the :method:`rs.syncFrom()` helper in :binary:`~bin.mongosh`:

```javascript
rs.syncFrom("hostname<:port>");
```
