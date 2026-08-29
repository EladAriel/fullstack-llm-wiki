---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/BSONRegExp.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.946753Z"
---
.. _server-bsonRegExp-method:

# BSONRegExp() (mongosh method)

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

Creates a new :ref:`BSON type <bson-types>` for a regular expression. 

## Syntax

``BSONRegExp`` has the following syntax:

**method:** BSONRegExp("<pattern>, "<flags>")

   .. list-table::
      :header-rows: 1
      :widths: 20 20 60

      * - Parameter

        - Type

        - Description

      * - ``pattern``

        - string

        - The regular expression pattern. You must not wrap the pattern
          with delimiter characters. 

      * - ``flag``

        - string

        - The regular expression flags. Characters in this argument are
          sorted alphabetically. 

.. _bsonRegExp-examples:

## Examples

### Insert a ``BSONRegExp()`` Object

Use the ``BSONRegExp()`` constructor to create the BSON regular expression.

.. code-block:: javascript

   var bsonRegExp = BSONRegExp("(?-i)AA_", "i")

Insert the object into the ``testbson`` collection.

.. code-block:: javascript

   db.testbson.insertOne( { foo: bsonRegExp } )

### Retrieve a ``BSONRegExp()`` Object

Query the ``testbson`` collection for the inserted document.

.. code-block:: javascript

   db.testbson.find( {}, {}, { bsonRegExp: true } )

You can see the binary BSON regular expressions stored in the collection.

.. code-block:: javascript
   :copyable: false

   [
     {
       _id: ObjectId('65e8ba8a4b3c33a76e6cacca'),
       foo: BSONRegExp('(?-i)AA_', 'i')
     }
   ]

If you set ``bsonRegExp`` to ``false``, ``mongosh`` returns an error:

.. io-code-block::
   :copyable: true

   .. input:: 
      :language: javascript

      db.testbson.find( {}, {}, { bsonRegExp: false })

   .. output:: 
      :language: javascript

      Uncaught:
      SyntaxError: Invalid regular expression: /(?-i)AA_/i: Invalid group