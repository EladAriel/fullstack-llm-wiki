---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/views/update-view.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.801303Z"
---
.. _manual-views-modify:
.. _manual-views-remove:

# Modify or Remove a View

**meta:** :description: Modify a view in MongoDB by either dropping and recreating it or using the `collMod` command.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

To remove a view, use the :method:`db.collection.drop()` method on the view.

To modify a view, you can either:

- Drop and recreate the view.
- Use the :dbcommand:`collMod` command.

## Example

Consider the following view named ``lowStock``:

.. code-block:: javascript

   db.createView(
      "lowStock",
      "products",
      [ { $match: { quantity: { $lte: 20 } } } ]
   )

### Drop and Recreate the View

The following commands modify ``lowStock`` by dropping and
recreating the view:

.. code-block:: javascript

   db.lowStock.drop()

   db.createView(
      "lowStock",
      "products",
      [ { $match: { quantity: { $lte: 10 } } } ]
   )

### Use the ``collMod`` Command

Alternatively, you can use the ``collMod`` command to modify the view:

.. code-block:: javascript

   db.runCommand( {
      collMod: "lowStock",
      viewOn: "products",
      "pipeline": [ { $match: { quantity: { $lte: 10 } } } ]
   } )