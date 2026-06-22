---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/bucket.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $bucket (aggregation stage)

## Definition

## Considerations

### `$bucket` and Memory Restrictions

The :pipeline:`$bucket` stage has a limit of 100 megabytes of RAM. By default, if the stage exceeds this limit, :pipeline:`$bucket` returns an error. To allow more space for stage processing, use the `allowDiskUse <aggregate-cmd-allowDiskUse>` option to enable aggregation pipeline stages to write data to temporary files.

> **Seealso:** `agg-pipeline-limits`

## Syntax

```javascript
{
  $bucket: {
      groupBy: <expression>,
      boundaries: [ <lowerbound1>, <lowerbound2>, ... ],
      default: <literal>,
      output: {
         <output1>: { <$accumulator expression> },
         ...
         <outputN>: { <$accumulator expression> }
      }
   }
}
```

The :pipeline:`$bucket` document contains the following fields:

## Behavior

:pipeline:`$bucket` requires at least one of the following conditions to be met or the operation throws an error:

- Each input document resolves the `groupBy <bucket-group-by>`
expression to a value within one of the bucket ranges specified by `boundaries <bucket-boundaries>`, or

- A `default <bucket-default>` value is specified to bucket
documents whose `groupBy` values are outside of the `boundaries` or of a different `BSON type <bson-types>` than the values in `boundaries`.

If the `groupBy` expression resolves to an array or a document, `$bucket` arranges the input documents into buckets using the comparison logic from :pipeline:`$sort`.

## Examples

## Learn More

To learn more about related pipeline stages, see the :pipeline:`$bucketAuto` guide.
