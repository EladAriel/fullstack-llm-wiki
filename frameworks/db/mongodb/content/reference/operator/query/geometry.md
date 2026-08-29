---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/geometry.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.244650Z"
---
# $geometry (query predicate operator)

**meta:** :description: Specify GeoJSON geometry for geospatial queries using `$geometry` with default or custom coordinate reference systems.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**query:** $geometry

   The :query:`$geometry` operator specifies a :term:`GeoJSON` geometry
   for use with the following geospatial query operators:
   :query:`$geoWithin`, :query:`$geoIntersects`, :query:`$near`, and
   :query:`$nearSphere`. :query:`$geometry` uses ``EPSG:4326`` as the
   default coordinate reference system (CRS).

   To specify GeoJSON objects with the default CRS, use the following
   prototype for :query:`$geometry`:

   .. code-block:: javascript

      $geometry: {
         type: "<GeoJSON object type>",
         coordinates: [ <coordinates> ]
      }

   To specify a single-ringed GeoJSON :ref:`polygon
   <geojson-polygon>` with a custom MongoDB CRS, use the following
   prototype (available only for :query:`$geoWithin` and
   :query:`$geoIntersects`):

   .. code-block:: javascript

      $geometry: {
         type: "Polygon",
         coordinates: [ <coordinates> ],
         crs: {
            type: "name",
            properties: { name: "urn:x-mongodb:crs:strictwinding:EPSG:4326" }
         }
      }

   The custom MongoDB coordinate reference system has a strict
   counter-clockwise winding order.

   .. include::  /includes/extracts/geospatial-long-lat-values.rst