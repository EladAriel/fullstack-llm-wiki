---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/each.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.103397Z"
---
# $each (update operator)

**meta:** :description: Utilize the `$each` modifier with `$addToSet` and `$push` operators to add multiple values to arrays in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**update:** $each

   The :update:`$each` modifier is available for use with the
   :update:`$addToSet` operator and the :update:`$push`
   operator.

   Use with the :update:`$addToSet` operator to add multiple values to
   an array ``<field>`` if the values do not exist in the ``<field>``.

   .. code-block:: javascript

      { $addToSet: { <field>: { $each: [ <value1>, <value2> ... ] } } }

   Use with the :update:`$push` operator to append multiple values to
   an array ``<field>``.

   .. code-block:: javascript

      { $push: { <field>: { $each: [ <value1>, <value2> ... ] } } }

   The :update:`$push` operator can use :update:`$each` modifier with
   other modifiers. For a list of modifiers available for
   :update:`$push`, see :ref:`push-modifiers`.

## Behavior

**include:** /includes/fact-update-operator-processing-order.rst

## Examples

### Use ``$each``  with ``$push`` Operator

**include:** /includes/example-push-each.rst

### Use ``$each``  with ``$addToSet`` Operator

**include:** /includes/example-addToSet-each.rst