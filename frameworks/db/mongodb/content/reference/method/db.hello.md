---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.hello.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.972981Z"
---
# db.hello() (mongosh method)

**meta:** :description: Use `db.hello()` to determine the role of a `mongod` instance within a replica set, indicating if it's primary or secondary.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** db.hello()

   .. versionadded:: 5.0

   Returns a document that describes the role of the :binary:`~bin.mongod`
   instance.

   If the :binary:`~bin.mongod` is a member of a :term:`replica set`, then
   the :data:`~hello.isWritablePrimary` and :data:`~hello.secondary`
   fields report if the instance is the :term:`primary` or if it is a
   :term:`secondary` member of the replica set.

   .. see::

      :dbcommand:`hello` for the complete documentation of
      the output of :method:`db.hello()`.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst