---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/manage-journaling.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# Configure Journaling for Self-Managed Deployments

MongoDB uses write ahead logging to an on-disk `journal` to guarantee `write operation <crud>` durability.

The WiredTiger storage engine does not require journaling to guarantee a consistent state after a crash. The database will be restored to the last consistent `checkpoint <storage-wiredtiger-checkpoints>` during recovery.  However, if MongoDB exits unexpectedly in between checkpoints, journaling is required to recover writes that occurred after the last checkpoint.

If :binary:`~bin.mongod` stops unexpectedly, the program can recover everything written to the journal. MongoDB will re-apply the write operations on restart and maintain a consistent state. By default, the greatest extent of lost writes, i.e., those not made to the journal, are those made in the last 100 milliseconds, plus the time it takes to perform the actual journal writes. See :setting:`~storage.journal.commitIntervalMs` for more information on the default.

## Procedures

### Get Commit Acknowledgement

You can get commit acknowledgment with the `write-concern` and the :writeconcern:`j` option. For details, see `write-concern-operation`.

### Monitor Journal Status

The :dbcommand:`serverStatus` command/:method:`db.serverStatus()` method returns :serverstatus:`wiredTiger.log`, which contains statistics on the journal.

### Recover Data After Unexpected Shutdown

On a restart after a crash, MongoDB replays all journal files in the journal directory before the server becomes available. If MongoDB must replay journal files, :binary:`~bin.mongod` notes these events in the log output.

There is no reason to run `--repair`.

### Change WiredTiger Journal Compressor

With the WiredTiger storage engine, MongoDB, by default, uses the `snappy` compressor for the journal. To specify a different compressions algorithm or no compression for a :binary:`~bin.mongod` instance:

> **Tip:** If you encounter an unclean shutdown for a :binary:`~bin.mongod`
during this procedure, you must use the old compressor settings to
recover using the journal files. Once recovered, you can retry the
procedure.
