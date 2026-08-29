---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/maxDistance.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.245380Z"
---
# $maxDistance (query predicate operator)

**meta:** :description: Constrain geospatial query results using `$maxDistance` to specify the maximum distance from a point in meters.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**query:** $maxDistance

   The :query:`$maxDistance` operator constrains the results of a
   geospatial :query:`$near` or :query:`$nearSphere` query to the
   specified distance. The measuring units for the maximum distance are
   determined by the coordinate system in use. For :term:`GeoJSON` point
   objects, specify the distance in meters, not radians. You must
   specify a non-negative number for :query:`$maxDistance`.

   The :ref:`2dsphere <2dsphere-index>` and :ref:`2d <2d-index>`
   geospatial indexes both support :query:`$maxDistance`: .

## Example

The following example query returns documents with location values that
are ``10`` or fewer units from the point ``[ -74 , 40 ]``.

.. code-block:: javascript

   db.places.find( {
      loc: { $near: [ -74 , 40 ],  $maxDistance: 10 }
   } )

MongoDB orders the results by their distance from ``[ -74 , 40 ]``.
The operation returns the first 100 results, unless you modify the
query with the :method:`cursor.limit()` method.