---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/revokeRolesFromRole.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.042130Z"
---
# revokeRolesFromRole (database command)

**meta:** :description: Remove specified inherited roles from a role using the `revokeRolesFromRole` command in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** revokeRolesFromRole

   Removes the specified inherited roles from a role. 

   .. |method| replace:: :method:`db.revokeRolesFromRole` helper method
   .. include:: /includes/fact-dbcommand-tip

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst
                
## Syntax

The command has the following syntax:

.. code-block:: javascript
  
   db.runCommand(
      {  
        revokeRolesFromRole: "<role>",
        roles: [
          { role: "<role>", db: "<database>" } | "<role>",
          ...
        ],
        writeConcern: { <write concern> },
        comment: <any>
      }
   )

## Command Fields

The command has the following fields:

.. list-table::
   :header-rows: 1
   :widths: 20 20 80
 
   * - Field
     - Type
     - Description

   * - ``revokeRolesFromRole``
     - string
     - The role from which to remove inherited roles.

   * - ``roles``
     - array
     - The inherited roles to remove.

   * - ``writeConcern``
     - document
     - .. include:: /includes/fact-write-concern-spec-link.rst

   * - ``comment``
     - any
     - .. include:: /includes/extracts/comment-content.rst

.. |local-cmd-name| replace:: :dbcommand:`revokeRolesFromRole`
**include:** /includes/fact-roles-array-contents.rst

## Required Access

**include:** /includes/access-revoke-roles.rst

## Example

The ``purchaseAgents`` role in the ``emea`` database inherits privileges
from several other roles, as listed in the ``roles`` array:

.. code-block:: javascript

   {
      "_id" : "emea.purchaseAgents",
      "role" : "purchaseAgents",
      "db" : "emea",
      "privileges" : [],
      "roles" : [
         {
            "role" : "readOrdersCollection",
            "db" : "emea"
         },
         {
            "role" : "readAccountsCollection",
            "db" : "emea"
         },
         {
            "role" : "writeOrdersCollection",
            "db" : "emea"
         }
      ]
   }

The following :dbcommand:`revokeRolesFromRole` operation on the ``emea``
database removes two roles from the ``purchaseAgents`` role:

.. code-block:: javascript

   use emea
   db.runCommand( { revokeRolesFromRole: "purchaseAgents",
                    roles: [
                             "writeOrdersCollection",
                             "readOrdersCollection"
                           ],
                     writeConcern: { w: "majority" , wtimeout: 5000 }
                } )

The ``purchaseAgents`` role now contains just one role:

.. code-block:: javascript

   {
      "_id" : "emea.purchaseAgents",
      "role" : "purchaseAgents",
      "db" : "emea",
      "privileges" : [],
      "roles" : [
         {
            "role" : "readAccountsCollection",
            "db" : "emea"
         }
      ]
   }