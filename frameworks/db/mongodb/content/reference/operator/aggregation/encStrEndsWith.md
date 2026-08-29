---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/encStrEndsWith.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.172607Z"
---
.. _qe-encstrendswith:

# $encStrEndsWith (expression operator)

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**versionadded:** 8.2

.. |command| replace:: ``$encStrEndsWith``

**include:** /includes/queryable-encryption/qe-aggregation-operator.rst

**expression:** $encStrEndsWith

   Returns ``true`` if the last characters of a string value match the
   characters in the specified string. The queried field must have :ref:`suffix
   queries enabled <qe-encryption-schema>`, and the length of the query string
   must be between the configured minimum and maximum number of characters,
   inclusive.

   By default, strings must match case and diacritical marks. 
   
   - Set :parameter:`caseSensitive` to ``false`` in the encryption schema for
     case-insensitive matching.
   
   - Set :parameter:`diacriticSensitive` to ``false`` in the encryption schema
     to disregard diacritic variations when matching.

   The :expression:`$encStrEndsWith` expression has the following
   :ref:`operator expression syntax <aggregation-expressions>`:

   .. code-block:: javascript

      { $encStrEndsWith: { input: ’$fieldname’, suffix: <target search key> } }


## Behavior

**include:** includes/queryable-encryption/qe-substring-search-behavior.rst

## Example

In :binary:`~bin.mongosh`:

.. code-block:: shell

   db.collection('MyCollection').aggregate([
      {
         $match: {
            $expr: {
               $encStrEndsWith: {
                  input: '$employeeFirstName',
                  suffix: 'son'
               }
            }
         }
      }
   ])