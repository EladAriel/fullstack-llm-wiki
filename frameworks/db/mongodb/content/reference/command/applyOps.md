---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/applyOps.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
