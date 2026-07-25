---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/bottom.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# $bottom (expression operator)

## Definition

> **Note:** This page describes the `$bottom` expression operator. For the `$bottom`
accumulator operator, see `$bottom (accumulator operator) <bottom_accumulator_operator>`.

## Syntax

When used as an expression operator, `$bottom` has the following syntax:

```none
{
   $bottom:
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

The following aggregation pipeline uses  `$bottom` on the `cast` array:

In this example, `$bottom` sorts the existing `cast` array in ascending alphabetical order and returns the last value.
