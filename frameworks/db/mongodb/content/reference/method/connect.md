---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/connect.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.918918Z"
---
# connect() (mongosh method)

**meta:** :description: Create a connection to a MongoDB instance using the `connect()` method, specifying the URL, user, and password parameters.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Description

**method:** connect(url, user, password)

   Creates a connection to a MongoDB instance and returns the reference
   to the database. However, in most cases, use the :method:`Mongo()`
   object and its :method:`~Mongo.getDB()` method instead.


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``url``
   
        - string
   
        - Specifies the connection string.
          You can specify either:
          
          - ``<hostname>:<port>/<database>``
          - ``<hostname>/<database>``
          - ``<database>``
          
          
   
      * - ``user``
   
        - string
   
        - Optional. Specifies an existing username with access privileges for this database.
          If ``user`` is specified, you must include the ``password`` parameter as well.
          
          
   
      * - ``password``
   
        - string
   
        - Optional unless the ``user`` parameter is specified. Specifies the
          password for the ``user``.
          
## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst

## Example

The following example instantiates a new connection to the MongoDB
instance running on the localhost interface and returns a reference
to ``myDatabase``:

.. code-block:: javascript

   db = connect("localhost:27017/myDatabase")

**seealso:** - :method:`Mongo()`
   - :method:`Mongo.getDB()`
   - :method:`db.auth()`