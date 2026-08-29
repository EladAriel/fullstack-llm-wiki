---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.getShardVersion.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.987993Z"
---
# db.collection.getShardVersion() (mongosh method)

**meta:** :description: Diagnose sharded cluster issues using the `db.collection.getShardVersion()` method, available in various MongoDB environments.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


**include:** /includes/fact-mongosh-shell-method.rst

## Definition

**method:** db.collection.getShardVersion()

   This method returns information regarding the state of data in a
   :term:`sharded cluster` that is useful when diagnosing underlying issues
   with a sharded cluster.

   For internal and diagnostic use only.

## Compatibility

.. |command| replace:: method

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst