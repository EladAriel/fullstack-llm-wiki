---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/expr.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================

# $expr (query predicate operator)

## Definition

.. versionchanged:: 5.0

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

```javascript
{ $expr: { <expression> } }
```

The argument can be any valid expression.

## Behavior

### $expr in $lookup Operations

When `$expr` appears in a :pipeline:`$match` stage that is part of a :pipeline:`$lookup` subpipeline, `$expr` can refer to `let` variables defined by the `$lookup` stage. For an example, see `lookup-multiple-joins`.

.. include:: /includes/expr-operators-and-indexes.rst

## Examples

.. include:: /includes/sample-data-usage.rst

### Compare Two Fields from a Single Document

.. include:: /includes/use-expr-in-find-query.rst

### Use $expr With Conditional Statements

Some queries need to execute conditional logic when defining a query filter. The aggregation pipeline provides the :expression:`$cond` operator to express conditional statements. By using `$expr` with the :expression:`$cond` operator, you can specify a conditional filter for your query statement.

Assume you want to calculate a weighted score for movies so that highly-rated movies with few votes do not dominate the results:

- If `imdb.votes` is greater than or equal to 1000, the weighted
score is the full `imdb.rating`.

- If `imdb.votes` is less than 1000, the weighted score is 0.5 of
the `imdb.rating`.

You would like to know which movies in the `movies` collection have a weighted score greater than `9`.

The following example uses `$expr` with :expression:`$cond` to calculate the weighted score based on `imdb.votes` and :expression:`$gt` to return documents whose calculated weighted score is greater than `9`:

The following table shows the weighted score for selected documents and whether the weighted score is greater than `9` (i.e. whether the document meets the query condition).

The :method:`db.collection.find()` operation returns 5 documents whose calculated weighted score is greater than `9`:

Even though :expression:`$cond` calculates a weighted score, that score is not reflected in the returned documents. Instead, the returned documents represent the matching documents in their original state.
