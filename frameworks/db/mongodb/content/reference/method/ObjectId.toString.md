---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ObjectId.toString.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.907642Z"
---
# ObjectId.toString() (mongosh method)

.. default-domain:: mongodb

**meta:** :description: Return the string representation of an ObjectId.

**facet:** :name: programming_language
   :values: shell

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** ObjectId.toString()

   Returns the string representation of the :method:`ObjectId()`.

## Compatibility

.. |operator-method| replace:: ``ObjectId.toString()``

**include:** /includes/fact-compatibility.rst

## Example

The following example:

- Generates a new :method:`ObjectId()` and stores it in the 
  variable ``myObjectId``.

- Creates a string representation of ``myObjectId`` using
  the :method:`toString()<ObjectId.toString()>` method.
  
- Stores the string representation in the variable ``myObjectIdString``.

Run the following commands in :binary:`mongosh`:

.. code-block:: javascript

   myObjectId = ObjectId("507c7f79bcf86cd7994f6c0e")
   myObjectIdString = myObjectId.toString()

The operation returns the following string:

.. code-block:: javascript
   :copyable: false

   507c7f79bcf86cd7994f6c0e

To confirm the type of ``myObjectIdString``, use the ``typeof`` JavaScript operator:

.. code-block:: javascript

   typeof myObjectIdString

The operation returns the following:

.. code-block:: javascript
   :copyable: false

   string