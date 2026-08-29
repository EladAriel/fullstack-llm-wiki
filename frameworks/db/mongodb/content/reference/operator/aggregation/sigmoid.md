---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/sigmoid.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.178481Z"
---
# $sigmoid  (expression operator)

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. Substitution used in includes and in the body of this text
.. |operatorName| replace:: ``$sigmoid``


## Definition

**expression:** $sigmoid

   Performs the sigmoid function, which calculates the percentile of a number in
   the normal distribution with standard deviation 1.

   The :expression:`$sigmoid` expression has the following syntax:

   .. code-block:: javascript

      { $sigmoid: { input: <numeric expression>, onNull: <expression>} }

   The arguments can be any valid :ref:`expression <aggregation-expressions>` as
   long as they resolve to all numbers.

   The sigmoid function is equivalent to the following algebraic operation:

   .. figure:: /images/sigmoid.png
      :alt: The sigmoid function
      :figwidth: 200px

## Example

This example uses a ``myScores`` collection that contains the following documents:

.. code-block:: javascript

   db.myScores.insertMany( [
      { score: 1 },
      { score: 5 },
      {},
      { score: 13 },
      { score: null },
      { score: 21 },
   ] )

The following aggregation pipeline adds a ``scaled`` field to each document and uses
``$sigmoid`` to calculate the ``scaled`` field value:

.. code-block:: javascript

   db.myScores.aggregate( [
      { $set: {
         scaled: { $sigmoid: "$score" }
      } }
   ] )

The operation returns the following documents:

.. code-block:: javascript
   :copyable: false

   { score: 1, scaled: 0.7310585786 }
   { score: 5, scaled: 0.9933071491 }
   { scaled: null }
   { score: 13, scaled: 0.9999977397 }
   { score: null, scaled: null }
   { score: 19, scaled: 0.9999999992 }