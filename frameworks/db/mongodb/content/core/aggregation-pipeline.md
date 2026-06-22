---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/aggregation-pipeline.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Aggregation Pipeline

.. include:: /includes/aggregation-pipeline-introduction.rst

When you run aggregation pipelines on {+atlas+} deployments in the {+atlas+} UI, you can preview the results at each stage.

## Complete Aggregation Pipeline Examples

The `aggregation-complete-examples` section contains step-by-step tutorials for common aggregation tasks, with examples for MongoDB Shell and each of the :driver:`official MongoDB drivers </>`.

## Additional Aggregation Pipeline Stage Details

An aggregation pipeline consists of one or more `stages <aggregation-pipeline-operator-reference>` that process documents:

- A stage does not need to output one document for every input
document. Some stages produce new documents or filter documents out.

- The same stage can appear multiple times in a pipeline, except for
:pipeline:`$out`, :pipeline:`$merge`, and :pipeline:`$geoNear`.

For all aggregation stages, see `aggregation-pipeline-operator-reference`.

### Expressions and Operators

Some aggregation pipeline stages accept `expressions <expression>`. Operators calculate values based on input expressions.

.. include:: /includes/expression-components.rst

### Field Paths

`Field path <field path>` expressions access fields in input documents. Prefix the field name with a dollar sign `$`. For example, `"$user"` references the `user` field, and `"$user.name"` references the embedded `user.name` field.

`"$<field>"` is equivalent to `"$$CURRENT.<field>"`, where :variable:`CURRENT` is a system variable that defaults to the root of the current object unless a stage specifies otherwise.

For more examples, see `agg-field-paths`.

## Run an Aggregation Pipeline

To run an aggregation pipeline, use:

- :method:`db.collection.aggregate()` or
- :dbcommand:`aggregate`
## Update Documents Using an Aggregation Pipeline

To update documents with an aggregation pipeline, use:

.. include:: /includes/table-update-with-aggregation-availability.rst

## Other Considerations

### Aggregation Pipeline Limitations

For limits on value types and result size, see `agg-pipeline-limits`.

### Aggregation Pipelines and Sharded Collections

Aggregation pipelines support operations on sharded collections. See `aggregation-pipeline-sharded-collection`.

### Aggregation Pipelines as an Alternative to Map-Reduce

.. include:: /includes/fact-use-aggregation-not-map-reduce.rst

### Accessing Array Element Indexes in $map, $filter, and $reduce

.. include:: /includes/array-element-index.rst

## Learn More

To learn more about aggregation pipelines, see:

- `aggregation-expression-operators`
- `aggregation-pipeline-operator-reference`
## Contents

- Field Paths </core/field-paths>
- Optimization </core/aggregation-pipeline-optimization>
- Limits </core/aggregation-pipeline-limits>
- Sharded Collections </core/aggregation-pipeline-sharded-collections>
- Complete Pipeline Examples </tutorial/aggregation-complete-examples>
