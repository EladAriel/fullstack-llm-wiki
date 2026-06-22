---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/facet.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $facet (aggregation stage)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The `$facet` stage has the following form:

```javascript
{ $facet:
    {
      <outputField1>: [ <stage1>, <stage2>, ... ],
      <outputField2>: [ <stage1>, <stage2>, ... ],
      ...

    }
}
```

Specify the output field name for each specified pipeline.

## Considerations

As each stage in a `$facet` executes, the resulting document is limited to 100 megabytes. Note the `allowDiskUse <aggregate-cmd-allowDiskUse>` flag doesn't affect the 100 megabyte size limit, since `$facet` can't spill to disk.

If a `$facet` stage constructs a document where the size exceeds the 100 megabyte limit, MongoDB returns an :error:`ExceededMemoryLimit <146>` error.

The final output document is subject to the 16 mebibyte :limit:`BSON document size limit <BSON Document Size>`. If it exceeds 16 mebibytes, the aggregation produces an error.

> **Seealso:** `agg-pipeline-limits`

## Behavior

Facet-related aggregation stages categorize and group incoming documents. Specify any of the following facet-related stages within different `$facet` sub-pipeline's `<stage>` to perform a multi-faceted aggregation:

- :pipeline:`$bucket`
- :pipeline:`$bucketAuto`
- :pipeline:`$sortByCount`
Other `aggregation stages <aggregation-pipeline-operator-reference>` can also be used with `$facet` with the following exceptions:

- :pipeline:`$collStats`
- `$facet`
- :pipeline:`$geoNear`
- :pipeline:`$indexStats`
- :pipeline:`$out`
- :pipeline:`$merge`
- :pipeline:`$planCacheStats`
- :pipeline:`$search`
- :pipeline:`$searchMeta`
- :pipeline:`$vectorSearch`
Each sub-pipeline within `$facet` is passed the exact same set of input documents. These sub-pipelines are completely independent of one another and the document array output by each is stored in separate fields in the output document. The output of one sub-pipeline can not be used as the input for a different sub-pipeline within the same `$facet` stage. If further aggregations are required, add additional stages after `$facet` and specify the field name, `<outputField>`, of the desired sub-pipeline output.

### Index Use

Pipeline order determines how the `$facet` stage uses indexes.

- If the `$facet` stage is the first stage in a pipeline, the stage
will perform a `COLLSCAN`. The `$facet` stage does not make use of indexes if it is the first stage in the pipeline.

- If the `$facet` stage comes later in the pipeline and earlier stages
have used indexes, `$facet` will not trigger a `COLLSCAN` during execution.

For example, :pipeline:`$match` or :pipeline:`$sort` stages that come before a `$facet` stage can make use of indexes and the `$facet` will not trigger a `COLLSCAN`.

For optimization suggestions, see: `agg-pipeline-optimization`.

## Examples

## Learn More

To learn more about related pipeline stages, see the :pipeline:`$bucketAuto`, :pipeline:`$sortByCount`, and :pipeline:`$limit` guides.
