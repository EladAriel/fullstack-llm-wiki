---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/setClusterParameter.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.092037Z"
---
# setClusterParameter (database command)

**meta:** :description: Modify cluster parameters across all nodes in a replica set or sharded cluster using the `setClusterParameter` command.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition
   

**dbcommand:** setClusterParameter

   :dbcommand:`setClusterParameter` is an administrative command for
   modifying values of **cluster parameters**. Cluster parameters 
   are configurable parameters which affect all nodes in a replica set or 
   sharded cluster. 
   
   You must issue the ``setClusterParameter`` command against the ``admin`` 
   database.

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-onprem-only.rst

**include:** /includes/fact-environments-no-atlas-support.rst

## Syntax

.. code-block:: javascript

   db.adminCommand( 
      { 
        setClusterParameter: { <parameter>: <value> } 
      } 
   )

For the available cluster parameters, including examples, see
:ref:`cluster-parameters`. 

## Behavior

- You can only run ``setClusterParameter`` on the ``admin`` database. If you run 
  the command on any other database, MongoDB returns an error.

- You can only run ``setClusterParameter`` on a replica set primary or on a 
  :term:`sharded cluster`. 

- You **cannot** run ``setClusterParameter`` on a standalone deployment. 

- ``setClusterParameter`` accepts only one parameter at a time.

### Accesss Control

When :ref:`authentication <authentication>` is enabled, ``setClusterParameter`` 
only works when authenticated as a user with a role that has access 
to the ``setClusterParameter`` action.

### Persistence

The parameter modifications made using ``setClusterParameter`` 
are persisted on replica sets and sharded clusters. This ensures that 
parameter modifications made using ``setClusterParameter`` survive 
restarts.

### Stable API

When using :ref:`Stable API <stable-api>` V1 with :ref:`apiStrict
<api-strict-desc>` set to ``true``, you cannot use
:dbcommand:`setClusterParameter` to modify cluster parameters.