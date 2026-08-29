---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.getDB.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.946443Z"
---
# Mongo.getDB() (mongosh method)

**meta:** :description: Access database objects using `Mongo.getDB()` in `mongosh` or JavaScript by specifying the database name.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Description

**method:** Mongo.getDB(<database>)

   Provides access to database objects from
   :binary:`~bin.mongosh` or from a JavaScript file.

   The :method:`Mongo.getDB()` method has the following parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``database``
   
        - string
   
        - The name of the database to access.
                  
## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst

## Example

The following example instantiates a new connection to the MongoDB
instance running on the localhost interface and returns a reference
to ``"myDatabase"``:

.. code-block:: javascript

   db = new Mongo().getDB("myDatabase");

**seealso:** :method:`Mongo()` and :doc:`/reference/method/connect`