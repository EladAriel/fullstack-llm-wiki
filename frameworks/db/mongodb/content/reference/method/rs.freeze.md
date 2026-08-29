---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.freeze.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.966321Z"
---
# rs.freeze() (mongosh method)

**meta:** :description: Make a replica set member ineligible to become primary for a specified duration using the `rs.freeze()` method.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Description

**method:** rs.freeze(seconds)

   Makes the current :term:`replica set` member ineligible to become
   :term:`primary` for the period specified.

   .. |dbcommand| replace:: :dbcommand:`replSetFreeze` command
   .. include:: /includes/fact-mongosh-shell-method-alt

   The :method:`rs.freeze()` method has the following parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``seconds``
   
        - number
   
        - The duration the member is ineligible to become primary.
          
## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-onprem-only.rst