---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/geoNear.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $geoNear (aggregation stage)

## Definition

## Behavior

### Distance Calculations

`$geoNear` calculates distance based on the nearest point of the input document's perimeter.

For example, if the input document is a shape, `$geoNear` identifies the point on the shape's perimeter that is nearest to the specified point and outputs the distance between the specified point and the shape's nearest point.

### Considerations

When using `$geoNear`, consider that:

- You can only use `$geoNear` as the first stage of a
pipeline.

- .. include:: /includes/extracts/geoNear-stage-index-requirement.rst
If you have more than one geospatial index on the collection, use the `keys` parameter to specify which field to use in the calculation. If you have only one geospatial index, `$geoNear` implicitly uses the indexed field for the calculation.

- .. include:: /includes/fact-geoNear-restrict-near-in-query.rst
- `$geoNear` no longer has a default limit of 100 documents.
- The `near` parameter supports the :ref:`let option
<geoNear_let_example>` and `bound let option <geoNear_bounded_let_example>`.

- You can use the `$geoNear` pipeline operator on any field
in a `time series collection <manual-timeseries-collection>`. However, you cannot use the `query` field for `$geoNear` on a time series collection.

- You can create `partial <index-type-partial>` and :ref:`2dsphere
<2dsphere-index>` indexes on any field in a `time series collection <manual-timeseries-collection>`.

- .. include:: /includes/fact-geo-near-geojson-validation.rst
## Examples

## Learn More

To learn more about related pipeline stages, see the :pipeline:`$limit` guide.
