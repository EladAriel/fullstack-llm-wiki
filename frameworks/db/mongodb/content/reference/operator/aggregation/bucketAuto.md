---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/bucketAuto.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $bucketAuto (aggregation stage)

## Definition

## Considerations

### `$bucketAuto` and Memory Restrictions

The :pipeline:`$bucketAuto` stage has a limit of 100 megabytes of RAM. By default, if the stage exceeds this limit, MongoDB automatically writes temporary files to disk. For details, see :parameter:`allowDiskUseByDefault`.

> **Seealso:** `/core/aggregation-pipeline-limits`

## Behavior

There may be less than the specified number of buckets if:

- The number of input documents is less than the specified number of
buckets.

- The number of unique values of the `groupBy` expression is less
than the specified number of `buckets`.

- The `granularity` has fewer intervals than the number of
`buckets`.

- The `granularity` is not fine enough to evenly distribute documents
into the specified number of `buckets`.

If the `groupBy` expression refers to an array or document, the values are arranged using the same ordering as in :pipeline:`$sort` before determining the bucket boundaries.

The even distribution of documents across buckets depends on the cardinality, or the number of unique values, of the `groupBy` field. If the cardinality is not high enough, the $bucketAuto stage may not evenly distribute the results across buckets.

### Granularity

The `$bucketAuto` accepts an optional `granularity` parameter which ensures that the boundaries of all buckets adhere to a specified [preferred number series](https://en.wikipedia.org/wiki/Preferred_number). Using a preferred number series provides more control on where the bucket boundaries are set among the range of values in the `groupBy` expression. They may also be used to help logarithmically and evenly set bucket boundaries when the range of the `groupBy` expression scales exponentially.

#### Renard Series

The Renard number series are sets of numbers derived by taking either the 5 :superscript:`th`, 10 :superscript:`th`, 20 :superscript:`th`, 40 :superscript:`th`, or 80 :superscript:`th` root of 10, then including various powers of the root that equate to values between 1.0 to 10.0 (10.3 in the case of `R80`).

Set `granularity` to `R5`, `R10`, `R20`, `R40`, or `R80` to restrict bucket boundaries to values in the series. The values of the series are multiplied by a power of 10 when the `groupBy` values are outside of the 1.0 to 10.0 (10.3 for `R80`) range.

The same approach is applied to the other Renard series to offer finer granularity, i.e., more intervals between 1.0 and 10.0 (10.3 for `R80`).

#### E Series

The E number series are similar to the `Renard series <renard-series>` in that they subdivide the interval from 1.0 to 10.0 by the 6 :superscript:`th`, 12 :superscript:`th`, 24 :superscript:`th`, 48 :superscript:`th`, 96 :superscript:`th`, or 192 :superscript:`nd` root of ten with a particular relative error.

Set `granularity` to `E6`, `E12`, `E24`, `E48`, `E96`, or `E192` to restrict bucket boundaries to values in the series. The values of the series are multiplied by a power of 10 when the `groupBy` values are outside of the 1.0 to 10.0 range. To learn more about the E-series and their respective relative errors, see [preferred number series](https://en.wikipedia.org/wiki/Preferred_number).

#### 1-2-5 Series

The `1-2-5` series behaves like a three-value `Renard series <renard-series>`, if such a series existed.

Set `granularity` to `1-2-5` to restrict bucket boundaries to various powers of the third root of 10, rounded to one significant digit.

#### Powers of Two Series

Set `granularity` to `POWERSOF2` to restrict bucket boundaries to numbers that are a power of two.

#### Comparing Different Granularities

The following operation demonstrates how specifying different values for `granularity` affects how `$bucketAuto` determines bucket boundaries.  A collection of `things have an id` numbered from 0 to 99:

```javascript
{ _id: 0 }
{ _id: 1 }
...
{ _id: 99 }
```

Different values for `granularity` are substituted into the following operation:

```javascript
db.things.aggregate( [
  {
    $bucketAuto: {
      groupBy: "$_id",
      buckets: 5,
      granularity: <granularity>
    }
  }
] )
```

The results in the following table demonstrate how different values for `granularity` yield different bucket boundaries:

## Examples

## Learn More

To learn more about related pipeline stages, see the :pipeline:`$bucket` guide.
