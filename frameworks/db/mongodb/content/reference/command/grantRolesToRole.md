---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/grantRolesToRole.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.087799Z"
---
# grantRolesToRole (database command)

**meta:** :description: Grant roles to a user-defined role using the `grantRolesToRole` command, specifying roles, write concern, and optional comments.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** grantRolesToRole

   Grants roles to a :ref:`user-defined role <user-defined-roles>`.

   .. |method| replace:: :method:`db.grantRolesToRole` helper method
   .. include:: /includes/fact-dbcommand-tip

   The :dbcommand:`grantRolesToRole` command affects roles on the
   database where the command runs. 

The command has the following syntax:

.. code-block:: javascript
   
   db.runCommand(
      {  
        grantRolesToRole: "<role>",
        roles: [
                   { role: "<role>", db: "<database>" },
                   ...
               ],
        writeConcern: { <write concern> },
        comment: <any>
      }
   )
  
The command has the following fields:

.. list-table::
   :header-rows: 1
   :widths: 20 20 80
 
   * - Field
     - Type
     - Description

   * - ``grantRolesToRole``
     - string
     - The name of a role to add subsidiary roles.

   * - ``roles``
     - array
     - An array of roles from which to inherit.

   * - ``writeConcern``
     - document
     - .. include:: /includes/fact-write-concern-spec-link.rst

   * - ``comment``
     - any
     - .. include:: /includes/extracts/comment-content.rst

.. |local-cmd-name| replace:: :dbcommand:`grantRolesToRole`
**include:** /includes/fact-roles-array-contents.rst

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst
             
## Behavior

A role can inherit privileges from other roles in its database. A role
created on the ``admin`` database can inherit privileges from roles in
any database.

## Required Access

**include:** /includes/access-grant-roles.rst

## Example


The following :dbcommand:`grantRolesToRole` command updates the
``productsReaderWriter`` role in the ``products`` database to :ref:`inherit
<inheritance>` the :ref:`privileges <privileges>` of the ``productsReader``
role in the ``products`` database:

.. code-block:: javascript

   use products
   db.runCommand(
      { grantRolesToRole: "productsReaderWriter",
        roles: [
                 "productsReader"
        ],
        writeConcern: { w: "majority" , wtimeout: 5000 }
      }
   )