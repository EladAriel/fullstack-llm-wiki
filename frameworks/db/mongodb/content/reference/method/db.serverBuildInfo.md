---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.serverBuildInfo.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.894808Z"
---
# db.serverBuildInfo() (mongosh method)

**meta:** :description: Access build information for a `mongod` instance using the `db.serverBuildInfo()` method, compatible with Atlas, Enterprise, and Community environments.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** db.serverBuildInfo()

   Provides a wrapper around the :dbcommand:`buildInfo` :term:`database
   command`. :dbcommand:`buildInfo` returns a document that contains
   an overview of parameters used to compile this :binary:`~bin.mongod`
   instance.


## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst