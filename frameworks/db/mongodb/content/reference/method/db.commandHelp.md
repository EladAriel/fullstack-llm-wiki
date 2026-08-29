---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.commandHelp.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.941111Z"
---
# db.commandHelp() (mongosh method)

**meta:** :description: Use `db.commandHelp(command)` to display help text for a specified database command in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Description

**method:** db.commandHelp(command)

   Displays help text for the specified :term:`database command`. See
   the :doc:`/reference/command`.

   The :method:`db.commandHelp()` method has the following parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``command``
   
        - string
   
        - The name of a :term:`database command`.
          
          
## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-limited-all.rst

**include:** /includes/fact-environments-onprem-only.rst