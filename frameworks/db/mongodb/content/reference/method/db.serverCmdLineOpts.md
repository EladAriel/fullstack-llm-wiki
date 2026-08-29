---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.serverCmdLineOpts.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.996951Z"
---
# db.serverCmdLineOpts() (mongosh method)

**meta:** :description: Retrieve the startup arguments and configuration options for a `mongod` or `mongos` instance using `db.serverCmdLineOpts()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** db.serverCmdLineOpts()

   Wraps the :dbcommand:`getCmdLineOpts`
   :term:`database command`.

   Returns a document that reports on the arguments and configuration
   options used to start the ``mongod`` or ``mongos`` instance.

   See :ref:`<configuration-options>`, :binary:`mongod`, and
   :binary:`mongos` for additional information on
   available MongoDB runtime options.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst