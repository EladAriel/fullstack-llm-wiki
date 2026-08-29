---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/size.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.245684Z"
---
# $size (query predicate operator)

.. default-domain:: mongodb

**facet:** :name: programming_language
   :values: shell

**meta:** :description: Use the $size operator to match arrays with the specified number of elements. $size helps you query documents based on the size of an array field.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**query:** $size

   The :query:`$size` operator matches any array with the number of
   elements specified by the argument.

## Compatibility

.. |operator-method| replace:: ``$size``

**include:** /includes/fact-compatibility.rst

Consider the following examples:

.. code-block:: javascript

   db.collection.find( { field: { $size: 2 } } );

This query returns all documents in ``collection`` where ``field`` is an
array with 2 elements. For example, the query returns
``{ field: [ red, green ] }`` and ``{ field: [ apple,
lime ] }`` but *not* ``{ field: fruit }`` or ``{ field: [
orange, lemon, grapefruit ] }``. To match fields with only one
element within an array use :query:`$size` with a value of 1, as
follows:

.. code-block:: javascript

   db.collection.find( { field: { $size: 1 } } );

:query:`$size` does not accept ranges of values. To select
documents based on fields with different numbers of elements,
create a counter field that you increment when you add elements to
a field.

Queries cannot use indexes for the :query:`$size` portion of a
query, although the other portions of a query can use indexes if
applicable.

## Syntax
   
A ``$size`` expression has the following syntax:

.. code-block:: javascript

   {
      <field>: {
         $size: <number>
      }
   }

## Additional Examples

**include:** /includes/arrays-additional-examples.rst

**seealso:** :method:`db.collection.find()`