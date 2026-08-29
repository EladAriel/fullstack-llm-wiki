---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.isCapped.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.934590Z"
---
# db.collection.isCapped() (mongosh method)

**meta:** :description: Determine if a collection is capped using the `db.collection.isCapped()` method, returning `true` for capped collections.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


**include:** /includes/fact-mongosh-shell-method-alt

## Definition

**method:** db.collection.isCapped()

   .. |dbcommand| replace:: :data:`~collStats.capped` field returned by the 
      :dbcommand:`collStats` command

   :returns: Returns ``true`` if the collection is a :term:`capped
             collection`, otherwise returns ``false``.

   .. seealso::

      :doc:`/core/capped-collections`

## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst