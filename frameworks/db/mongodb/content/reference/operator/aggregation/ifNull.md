---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/ifNull.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# $ifNull (expression operator)

## Definition

The :expression:`$ifNull` expression evaluates input expressions for null values and returns:

- The first non-null input `expression <aggregation-expressions>`
value found.

- A replacement `expression <aggregation-expressions>` value if all
input expressions evaluate to null.

:expression:`$ifNull` treats undefined values and missing fields as null.

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

```none
{
   $ifNull: [
      <input-expression-1>,
      ...
      <input-expression-n>,
      <replacement-expression-if-null>
   ]
}
```

## Examples

.. include:: /includes/sample-data-usage.rst

### Single Input Expression

The following example uses :expression:`$ifNull` to return:

- `rated` if the `rated` field is non-null.
- `"Not Rated"` string if `rated` is null or missing.
### Multiple Input Expressions

.. versionadded:: 5.0

The following example uses :expression:`$ifNull` to return:

- `tomatoes.critic.rating` if it's non-null.
- `tomatoes.viewer.rating` if `tomatoes.critic.rating` is null
or missing and `tomatoes.viewer.rating` is non-null.

- `0` if both `tomatoes.critic.rating` and
`tomatoes.viewer.rating` are null or missing.
