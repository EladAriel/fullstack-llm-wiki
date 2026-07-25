---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/cond.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================

# $cond (expression operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :expression:`$cond` expression has one of two syntaxes:

```javascript
{ $cond: { if: <boolean-expression>, then: <true-case>, else: <false-case> } }
```

Or:

```javascript
{ $cond: [ <boolean-expression>, <true-case>, <false-case> ] }
```

:expression:`$cond` requires all three arguments (`if-then-else`) for either syntax.

If the `<boolean-expression>` evaluates to `true`, then :expression:`$cond` evaluates and returns the value of the `<true-case>` expression. Otherwise, :expression:`$cond` evaluates and returns the value of the `<false-case>` expression.

The arguments can be any valid `expression <aggregation-expressions>`.

> **Seealso:** :expression:`$switch`

## Examples

.. include:: /includes/sample-data-usage.rst

The following aggregation operation uses the :expression:`$cond` expression to assign a rental price to each movie. The operation prices movies with an `imdb.rating` greater than or equal to `9` at `5.99`. The operation prices all other movies at `3.99`:

The following operation uses the array syntax of the :expression:`$cond` expression and returns the same results:
