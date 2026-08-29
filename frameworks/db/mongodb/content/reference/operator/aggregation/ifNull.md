---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/ifNull.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.193210Z"
---
# $ifNull (expression operator)

.. default-domain:: mongodb

**facet:** :name: programming_language
   :values: shell

**meta:** :description: Learn how to use an aggregation operator to evaluate expressions for null values and return or replace null values.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**expression:** $ifNull

The :expression:`$ifNull` expression evaluates input expressions for
null values and returns:
   
- The first non-null input :ref:`expression <aggregation-expressions>`
  value found.
   
- A replacement :ref:`expression <aggregation-expressions>` value if all
  input expressions evaluate to null.
     
:expression:`$ifNull` treats undefined values and missing fields as
null.
   
## Compatibility

.. |operator-method| replace:: ``$ifNull``

**include:** /includes/fact-compatibility.rst

## Syntax

.. code-block:: none
   :copyable: false

   {
      $ifNull: [
         <input-expression-1>,
         ...
         <input-expression-n>,
         <replacement-expression-if-null>
      ]
   }

## Examples

**include:** /includes/sample-data-usage.rst

### Single Input Expression

The following example uses :expression:`$ifNull` to return:

- ``rated`` if the ``rated`` field is non-null.

- ``"Not Rated"`` string if ``rated`` is null or missing.

.. io-code-block::
   :copyable: true

   .. input:: /code-examples/tested/command-line/mongosh/aggregation/expressions/ifNull/single-input.snippet.if-null-single-input.js
      :language: javascript
      :category: usage example

   .. output:: /code-examples/tested/command-line/mongosh/aggregation/expressions/ifNull/single-input-output.sh
      :language: javascript

### Multiple Input Expressions

**versionadded:** 5.0

The following example uses :expression:`$ifNull` to return:

- ``tomatoes.critic.rating`` if it's non-null.

- ``tomatoes.viewer.rating`` if ``tomatoes.critic.rating`` is null
  or missing and ``tomatoes.viewer.rating`` is non-null.

- ``0`` if both ``tomatoes.critic.rating`` and
  ``tomatoes.viewer.rating`` are null or missing.

.. io-code-block::
   :copyable: true

   .. input:: /code-examples/tested/command-line/mongosh/aggregation/expressions/ifNull/multiple-input.snippet.if-null-multiple-input.js
      :language: javascript
      :category: usage example

   .. output:: /code-examples/tested/command-line/mongosh/aggregation/expressions/ifNull/multiple-input-output.sh
      :language: javascript