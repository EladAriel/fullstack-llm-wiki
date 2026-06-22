---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/documents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $documents (aggregation stage)

## Definition

## Syntax

The :pipeline:`$documents` stage has the following form:

```
{ $documents: <expression> }
```

## Limitations

- You can only use `$documents` in a database-level aggregation
pipeline.

- You must use `$documents` as the first stage of an aggregation
pipeline.

See below for `usage examples <ex-agg-documents-stage>`.

## Behavior

:pipeline:`$documents` accepts any valid expression that resolves to an array of objects. This includes:

- system variables, such as :variable:`$$NOW <NOW>` or
`$$SEARCH_META`

- :expression:`$let` expressions
- variables in scope from :pipeline:`$lookup` expressions
Expressions that do not resolve to a current document, like `$myField` or :variable:`$$ROOT <ROOT>`, will result in an error.

## Examples

## Learn More

For details on subqueries using the :pipeline:`$lookup` syntax, see `lookup-syntax-concise-correlated-subquery`.
