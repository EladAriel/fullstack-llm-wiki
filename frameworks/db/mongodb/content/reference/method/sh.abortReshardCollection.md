---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.abortReshardCollection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.947760Z"
---
# sh.abortReshardCollection() (mongosh method)

**meta:** :description: Abort a resharding operation using `sh.abortReshardCollection()` before the commit phase in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.abortReshardCollection(namespace)

   .. versionadded:: 5.0

   During a :ref:`resharding operation <sharding-resharding>`, you can
   abort the operation with the :method:`sh.abortReshardCollection()`
   method.

   You can abort a :ref:`resharding operation <sharding-resharding>` at
   any point until the :ref:`commit phase
   <resharding-commit-phase-method>`. If the
   :ref:`resharding operation <sharding-resharding>` has reached the
   :ref:`commit phase <resharding-commit-phase-method>` before you run
   the :method:`sh.abortReshardCollection()` method, the method returns
   an error.

   .. |dbcommand| replace:: :dbcommand:`abortReshardCollection` command
   .. include:: /includes/fact-mongosh-shell-method-alt.rst

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`sh.abortReshardCollection()` method has the following syntax:

.. code-block:: javascript

   sh.abortReshardCollection( <namespace> )

### Parameter

The :method:`sh.abortReshardCollection()` method takes the following
parameter:

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Parameter
     - Type
     - Description

   * - :ref:`namespace <method-abortReshardCollection-namespace>`

     - String

     - .. _method-abortReshardCollection-namespace:

       The name of the collection to shard in the form
       ``"<database>.<collection>"``.

## Example

### Abort a Resharding Operation

The following example aborts a running :ref:`resharding operation
<sharding-resharding>` on the ``sales.orders`` collection:

.. code-block:: javascript

   sh.abortReshardCollection("sales.orders")

**seealso:** :ref:`sharding-resharding`