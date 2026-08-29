---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql/projection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.861565Z"
---
.. _projection-operators-ref:

# Find Command Projection Operators

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The following linked pages describe specialized operators available only
in find command projections. You can also use non-specialized
:ref:`expressions <operator-ref-landing>` in find command projections.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description

   * - :projection:`$`
     - Projects the first array element that matches the query condition.

   * - :projection:`$elemMatch`
     - Projects the first array element that matches the specified :projection:`$elemMatch` condition.

   * - :expression:`$meta`
     - Projects the available per-document metadata.

   * - :projection:`$slice`
     - Limits the number of elements projected from an array. Supports
       skip and limit slices.
     
**note:** View Support

   :method:`~db.collection.find()` operations on views do not support
   any of the preceding projection operators.

**toctree:** :titlesonly: 
   :hidden: 

   $ </reference/operator/projection/positional>
   $elemMatch </reference/operator/projection/elemMatch>
   $slice </reference/operator/projection/slice>