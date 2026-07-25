---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/encStrContains.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================================

# $encStrContains (expression operator)

## Definition

.. versionadded:: 8.2

.. include:: /includes/queryable-encryption/qe-aggregation-operator.rst

## Behavior

.. include:: includes/queryable-encryption/qe-substring-search-behavior.rst

## Example

In :binary:`~bin.mongosh`:

```shell
db.collection('MyCollection').aggregate([
   {
      $match: {
         $expr: {
            $encStrContains: {
               input: '$employeeLastName',
               substring: 'earso'
            }
         }
      }
   }
])
```

To match multiple fields:

```shell
db.collection('MyCollection').aggregate([
   {
      $match: {
         $expr: {
            $and: [
               {
                  $encStrContains: {
                     input: '$employeeLastName',
                     substring: 'earso'
                  }
               },
               {
                  $encStrContains: {
                     input: '$employeeFirstName',
                     substring: 'John'
                  }
               }
            ]
         }
      }
   }
])
```
