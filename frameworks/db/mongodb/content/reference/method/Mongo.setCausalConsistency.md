---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.setCausalConsistency.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.940594Z"
---
# Mongo.setCausalConsistency() (mongosh method)

**meta:** :description: Enable or disable causal consistency on a MongoDB connection object using the `setCausalConsistency` method.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** Mongo.setCausalConsistency(<boolean>)

   Enables or disables :ref:`causal consistency <causal-consistency>`
   on the connection object. Causal consistency is disabled on the
   connection object by default.
   
   .. note::

      The :method:`Mongo` connection object may have causal consistency
      disabled even though sessions may have causal consistency enabled
      or vice versa. See :method:`Mongo.startSession()`.

   To enable causal consistency for the connection object, call the
   method without any argument:

   .. code-block:: javascript
   
      var conn = Mongo("localhost:27017");
      conn.setCausalConsistency();

   The method also can accept a boolean argument:

   - ``true`` to enable causal consistency:

     .. code-block:: javascript

        conn.setCausalConsistency(true);

   - ``false`` to disable causal consistency:

     .. code-block:: javascript

        conn.setCausalConsistency(false);

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst

## Example

The following :binary:`~bin.mongosh` operation enables causal
consistency on the :method:`Mongo` connection object associated with
:binary:`~bin.mongosh`'s global ``db`` variable:

.. code-block:: javascript

   db.getMongo().setCausalConsistency();

**seealso:** - :method:`db.getMongo()`