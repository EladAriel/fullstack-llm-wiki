---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.readConcern.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.986962Z"
---
# cursor.readConcern() (mongosh method)

**meta:** :description: Specify a read concern level for the `db.collection.find()` method using `cursor.readConcern(level)` in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


## Definition

**method:** cursor.readConcern(level)


   .. include:: /includes/fact-mongosh-shell-method.rst

   Specify a :term:`read concern` for the :method:`db.collection.find()`
   method.

   The :method:`~cursor.readConcern()` method has the following form:

   .. code-block:: javascript

      db.collection.find().readConcern(<level>)

   The :method:`~cursor.readConcern()` method has the following
   parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``level``
   
        - string
   
        - :term:`Read concern <read concern>` level.
          
          .. include:: /includes/fact-readConcern-option-description.rst
          
          
## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst   


## Considerations

### Read Your Own Writes

**include:** /includes/fact-read-own-writes.rst

### Linearizable Read Concern Performance

**include:** /includes/extracts/maxTimeMS-readConcern-cursor.rst

.. code-block:: javascript

   db.restaurants.find( { _id: 5 } ).readConcern("linearizable").maxTimeMS(10000)


**seealso:** :doc:`/reference/read-concern`