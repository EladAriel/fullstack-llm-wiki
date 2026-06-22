---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.status.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# rs.status() (mongosh method)

## Definition

## Compatibility

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Output

For an example and details on the output, see `replSetGetStatus <rs-status-output>`.

If you run the :binary:`~bin.mongosh` helper method :method:`rs.status()` (or the :dbcommand:`replSetGetStatus` command) on a member during its `initial sync <replica-set-initial-sync>` (i.e. :replstate:`STARTUP2` state), the command returns `replSetGetStatus.initialSyncStatus` metrics.

Once the member completes its initial sync, the `replSetGetStatus.initialSyncStatus` metrics becomes unavailable.
