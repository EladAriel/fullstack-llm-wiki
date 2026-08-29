---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql/query-predicates/geospatial.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.099115Z"
---
.. _geospatial-query-operators:
.. _query-selectors-geospatial:
.. _geospatial-query-selectors:

# Geospatial Query Predicate Operators

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

Geospatial operators return data based on geospatial expression 
conditions.

## Query Predicate Operators

**include:** /includes/geospatial-query-predicate-operators.rst

## Geometry Specifiers

Use the following specifiers in geospatial query predicates to specify
geometric elements to query against.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name

     - Description

   * - :query:`$box`

     - Specifies a rectangular box using legacy coordinate pairs for
       :query:`$geoWithin` queries. The :ref:`2d <2d-index>` index
       supports :query:`$box`.

   * - :query:`$center`

     - Specifies a circle using legacy coordinate pairs to
       :query:`$geoWithin` queries when using planar geometry. The
       ``2d`` index supports :query:`$center`.

   * - :query:`$centerSphere`

     - Specifies a circle using either legacy coordinate pairs or
       :term:`GeoJSON` format for :query:`$geoWithin` queries when using
       spherical geometry. The :ref:`2dsphere <2dsphere-index>` and
       :ref:`2d <2d-index>` indexes support :query:`$centerSphere`.

   * - :query:`$geometry`

     - Specifies a geometry in :term:`GeoJSON` format to geospatial query operators.

   * - :query:`$maxDistance`

     - Specifies a maximum distance to limit the results of :query:`$near`
       and :query:`$nearSphere` queries. The ``2dsphere``
       and ``2d`` indexes support :query:`$maxDistance`.

   * - :query:`$minDistance`

     - Specifies a minimum distance to limit the results of :query:`$near`
       and :query:`$nearSphere` queries. For use with ``2dsphere`` index
       only.

   * - :query:`$polygon`

     - Specifies a polygon to using legacy coordinate pairs for
       :query:`$geoWithin` queries. The ``2d`` index supports
       :query:`$polygon`.

**toctree:** :titlesonly: 
   :hidden: 

   $box </reference/operator/query/box>
   $center </reference/operator/query/center>
   $centerSphere </reference/operator/query/centerSphere>
   $geoIntersects </reference/operator/query/geoIntersects>
   $geometry </reference/operator/query/geometry>
   $geoWithin </reference/operator/query/geoWithin>
   $maxDistance </reference/operator/query/maxDistance>
   $minDistance </reference/operator/query/minDistance>
   $near </reference/operator/query/near>
   $nearSphere </reference/operator/query/nearSphere>
   $polygon </reference/operator/query/polygon>