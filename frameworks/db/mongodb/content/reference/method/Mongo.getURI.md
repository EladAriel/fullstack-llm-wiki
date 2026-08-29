---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.getURI.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.967310Z"
---
# Mongo.getURI() (mongosh method)

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** Mongo.getURI()

   :returns: The connection string for the current active connection.

   See the :ref:`mongodb-uri` for more information.

## Syntax

The command takes the following form:

.. code-block:: javascript

   db.getMongo().getURI()

You can use this method to return a URI string for a connection, which
you can then use to create a new ``Mongo()`` instance:

.. code-block:: javascript 

   new Mongo(db.getMongo().getURI())

## Example

To return the current connection string, enter the following:

.. io-code-block:: 
   :copyable: true

   .. input:: 
      :language: js 
      
      db.getMongo().getURI()

   .. output:: 
      :language: js 
      
      mongodb://127.0.0.1:27019/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.4