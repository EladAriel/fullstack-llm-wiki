---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/applyOps.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# applyOps (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

.. include:: /includes/warning-blocking-global.rst

## Required Access

If the specified `oplog` entries contain `collection UUIDs <collections-uuids>`, executing this command requires both the :authaction:`useUUID` and :authaction:`forceUUID` privileges on the cluster resource to which the oplog entries are attempting to be written.
