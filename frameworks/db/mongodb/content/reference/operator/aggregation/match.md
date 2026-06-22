---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/match.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $match (aggregation stage)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

```javascript
{ $match: { <query predicate> } }
```

The syntax for the `$match` query predicate is identical to the syntax used in the `query <method-find-query>` argument of a :method:`~db.collection.find()` command.

## Behavior

### Pipeline Optimization

- Place the :pipeline:`$match` as early in the aggregation
`pipeline` as possible. Because :pipeline:`$match` limits the total number of documents in the aggregation pipeline, earlier :pipeline:`$match` operations minimize the amount of processing down the pipe.

- If you place a :pipeline:`$match` at the very beginning of a
pipeline, the query can take advantage of `indexes <index>` like any other :method:`db.collection.find()` or :method:`db.collection.findOne()`.

### Expressions in Query Predicates

To include `expressions <aggregation-expressions>` in a query predicate, use the :query:`$expr` operator.

### 0, Null, False or Missing Values

A `$match` stage filters out a document from pipeline results if one of the following conditions applies:

- The `$match` query predicate returns a `0`, `null`, or `false`
value on that document.

- The `$match` query predicate uses a field that is missing from
that document.

### Restrictions

- You cannot use :query:`$where` in a `$match` stage.
- You cannot use :query:`$near` or :query:`$nearSphere` in a `$match`
stage. As an alternative, you can either:

- Use the :pipeline:`$geoNear` stage instead of the :pipeline:`$match`
stage.

- Use the :query:`$geoWithin` query predicate operator with
:query:`$center` or :query:`$centerSphere` in the :pipeline:`$match` stage.

- To use :query:`$text` in a :pipeline:`$match` stage, the
:pipeline:`$match` stage has to be the first stage of the pipeline.

.. include:: /includes/extracts/views-unsupported-text-search.rst

### Filter Data on Atlas by Using {+fts+}

For data stored in :atlas:`{+atlas+} </>`, you can use the :atlas:`{+fts+} </atlas-search>` `compound-ref` operator `filter` option to match or filter documents when running :pipeline:`$search` queries. Running :pipeline:`$match` after :pipeline:`$search` is less performant than running :pipeline:`$search` with the `compound-ref` operator `filter` option.

To learn more about the `filter` option, see `compound-ref` in the Atlas documentation.

## Examples

## Learn More

Refer to the `aggregation-complete-examples` for more information and use cases on aggregation.
