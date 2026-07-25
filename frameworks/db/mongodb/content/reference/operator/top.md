---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/top.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# $top (expression operator)

## Definition

> **Note:** This page describes the `$top` expression operator. For the `$top`
accumulator operator, see `$top (accumulator operator) <top_accumulator_operator>`.

## Syntax

When used as an expression operator, `$top` has the following syntax:

```none
{
   $top:
      {
         sortBy: <expression>,
         input: <expression>
      }
}
```

## Behavior

### Sort Behavior

.. include:: /includes/sortBy-examples.rst

### Input Values

The `input` field must resolve to an array. If you specify an `input` that is not an array, MongoDB errors.

## Example

.. include:: /includes/sample-data-usage-singular.rst

The `movies` collection contains documents that resemble the following example:

The following aggregation pipeline uses `$top` on the `cast` array to return the first cast member in alphabetical order for a specified movie:

In this example, `$top` sorts the existing `cast` array in ascending alphabetical order and returns the first value.
