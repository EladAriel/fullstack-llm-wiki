---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/unset.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.105223Z"
---
# $unset (update operator)

.. default-domain:: mongodb

**facet:** :name: programming_language
   :values: shell

**meta:** :description: Learn how to delete specific fields in MongoDB documents using the $unset operator.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**note:** Disambiguation

   The following page refers to the update operator :update:`$unset`.
   For the aggregation stage, see :pipeline:`$unset`.

**update:** $unset

   The :update:`$unset` operator deletes a particular field.

## Compatibility

.. |operator-method| replace:: ``$unset``

**include:** /includes/fact-compatibility.rst

## Syntax

The :update:`$unset` operator has the following form:

.. code-block:: javascript

   { $unset: { <field1>: "", ... } }

The specified value in the :update:`$unset` expression (that is,
``""``) does not impact the operation.

**include:** /includes/use-dot-notation.rst

## Behavior

**include:** /includes/fact-update-operator-processing-order.rst

If the field does not exist, then :update:`$unset` does nothing (that
is, no operation).

When used with :update:`$` to match an array element, :update:`$unset`
replaces the matching element with ``null`` rather than removing the
matching element from the array. This behavior keeps consistent the
array size and element positions.

**include:** /includes/extracts/update-operation-empty-operand-expressions-unset.rst

## Example

**include:** /includes/sample-data-usage.rst

The following example uses the :update:`$unset` operator to remove
the ``label`` and ``status`` fields from the matching movie document:

**literalinclude:** /code-examples/tested/command-line/mongosh/operators/unset/unset-fields.snippet.unset-fields.js
   :language: javascript
   :category: usage example

The operation returns the following result:

**literalinclude:** /code-examples/tested/command-line/mongosh/operators/unset/unset-fields-output.sh
   :language: javascript
   :copyable: false
   :category: usage example

**seealso:** :method:`db.collection.updateMany()`
   :method:`db.collection.findAndModify()`
