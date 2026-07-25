---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/encStrNormalizedEq.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================================

# $encStrNormalizedEq (expression operator)

## Definition

.. versionadded:: 8.2

.. include:: /includes/queryable-encryption/qe-aggregation-operator.rst

## Behavior

- Case sensitivity and diacritical mark sensitivity are determined by the
configuration of the associated text search index.

.. include:: includes/queryable-encryption/qe-substring-search-behavior.rst

## Example

Consider the character é, which can be represented two ways:

- One code point, `U+00E9` (Latin small letter E with acute)
- Two code points, `U+0065` (Latin small letter E) followed by `U+0301`
(combining acute accent)

When comparing these two different representations of the name Béatrice:

- Using :expression:`$eq` evaluates to `false`, because the binary
representations are different.

- Using `$encStrNormalizedEq` evaluates to `true`, regardless of the
:parameter:`diacriticSensitive` setting, because the operator normalizes both strings prior to comparing them.

In :binary:`~bin.mongosh`:

```shell
db.collection('MyCollection').aggregate([
   {
      $match: {
         $expr: {
            $encStrNormalizedEq: {
               input: '$employeeLastName',
               string: 'Béatrice'
            }
         }
      }
   }
])
```
