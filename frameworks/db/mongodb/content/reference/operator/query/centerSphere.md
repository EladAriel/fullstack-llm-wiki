---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/centerSphere.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.243126Z"
---
# $centerSphere (query predicate operator)

**meta:** :description: Define a circle for geospatial queries using spherical geometry with the `$centerSphere` operator, specifying center coordinates and radius in radians.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**query:** $centerSphere

   Defines a circle for a :term:`geospatial` query that uses spherical
   geometry. The query returns documents that are within the bounds of
   the circle. You can use the :query:`$centerSphere` operator on both
   :term:`GeoJSON` objects and legacy coordinate pairs.

   To use :query:`$centerSphere`, specify an array that contains:

   - The grid coordinates of the circle's center point, and

   - The circle's radius measured in radians. To calculate radians, see
     :ref:`calculate-distance-spherical-geometry`.

   .. code-block:: javascript

      {
         <location field>: {
            $geoWithin: { $centerSphere: [ [ <x>, <y> ], <radius> ] }
         }
      }

   .. important::
      If you use longitude and latitude, specify **longitude first**.

## Behavior

.. |operator| replace:: :query:`$centerSphere`
**include:** /includes/note-geospatial-index-must-exist.rst

Both :ref:`2dsphere <2dsphere-index>` and :ref:`2d <2d-index>`
geospatial indexes support :query:`$centerSphere`.

## Example

The following example queries grid coordinates and returns all
documents within a 10 mile radius of longitude ``88 W`` and latitude
``30 N``. The query converts the distance to radians by dividing by the
approximate equatorial radius of the earth, 3963.2 miles:

.. code-block:: javascript

   db.places.find( {
     loc: { $geoWithin: { $centerSphere: [ [ -88, 30 ], 10/3963.2 ] } }
   } )