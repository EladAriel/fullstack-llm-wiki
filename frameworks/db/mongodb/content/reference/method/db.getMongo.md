---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getMongo.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.908825Z"
---
# db.getMongo() (mongosh method)

**meta:** :description: Access the current database connection in `mongosh` using `db.getMongo()` to verify connectivity.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**include:** /includes/fact-mongosh-shell-method.rst

**method:** db.getMongo()

   :returns: The current database connection.

   :method:`db.getMongo()` runs when the shell initiates. Use this
   command to test that :binary:`~bin.mongosh` has a connection to
   the proper database instance.

**note:** The legacy :binary:`mongo` shell has a sub-command,
   ``db.getMongo().setSecondaryOk()``, which is not available in
   :binary:`mongosh`. In :binary:`mongosh`, use
   :method:`Mongo.setReadPref()` instead.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst