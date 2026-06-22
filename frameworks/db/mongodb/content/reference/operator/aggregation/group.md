---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/group.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $group (aggregation stage)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :pipeline:`$group` stage has the following prototype form:

```javascript
{
 $group:
   {
     _id: <expression>, // Group key
     <field1>: { <accumulator1> : <expression1> },
     ...
   }
 }
```

The `_id` and the `accumulator operators <accumulators-group>` can accept any valid `expression`. For more information on expressions, see `aggregation-expressions`.

## Considerations

### Performance

.. include:: /includes/blocking-performance.rst

### Accumulator Operator

The `<accumulator>` operator must be one of the following accumulator operators:

.. include:: /includes/extracts/agg-operators-accumulators-group.rst

### `$group` and Memory Restrictions

If the :pipeline:`$group` stage exceeds 100 megabytes of RAM, MongoDB writes data to temporary files. However, if the `allowDiskUse <aggregate-cmd-allowDiskUse>` option is set to `false`, `$group` returns an error. For more information, refer to `aggregation pipeline limits <agg-pipeline-limits>`.

### `$group` Performance Optimizations

This section describes optimizations to improve the performance of :pipeline:`$group`. There are optimizations that you can make manually and optimizations MongoDB makes internally.

Optimization to Return the First or Last Document of Each Group ```````````````````````````````````````````````````````````````

If a pipeline :pipeline:`sorts <$sort>` and :pipeline:`groups <$group>` by the same field and the `$group` stage only uses the :group:`$first` or :group:`$last` accumulator operator, consider adding an `index <indexes>` on the grouped field which matches the sort order. In some cases, the `$group` stage can use the index to quickly find the first or last document of each group.

|sbe-title| ```````````

.. include:: /includes/fact-sbe-group-overview.rst

For more information, see `agg-group-optimization-sbe`.

## Examples

## Learn More

The `agg-example-group-data` tutorial provides an extensive example of the :pipeline:`$group` operator in a common use case.

To learn more about related pipeline stages, see the :pipeline:`$addFields` guide.
