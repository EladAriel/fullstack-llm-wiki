---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/similarityDotProduct.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# $similarityDotProduct (expression operator)

## Definition

.. versionadded:: 8.3

## Behavior

### `null` and Missing Values

If either argument resolves to `null` or refers to a missing field, :expression:`$similarityDotProduct` returns `null`.

### Return Value

:expression:`$similarityDotProduct` returns a `double`. When `score` is `false` (the default), the result is the raw dot product. The value depends on the magnitude of the input vectors. Vectors with larger magnitudes produce larger dot product values.

When `score` is `true`, the result is normalized using the formula `(1 + dotProduct) / 2`. This normalization assumes unit-length (normalized) input vectors. For unit-length vectors, the raw dot product is in the range `[-1, 1]` and the normalized score is in the range `[0, 1]`.

### Errors

:expression:`$similarityDotProduct` returns an error in the following cases:

- Either argument does not resolve to an array or `binData` value.
- Input arrays or `binData` values have different lengths.
- Either array contains non-numeric elements.
## Example

The following example uses a `vectors` collection:

```javascript
db.vectors.insertMany( [
   { _id: 1, a: [1, 2, 3], b: [1, 2, 3] },
   { _id: 2, a: [1, 2, 3], b: [3, 2, 1] },
   { _id: 3, a: [1, 2, 3], b: [4, 5, 6] }
] )
```

The following aggregation pipeline computes the dot product between the `a` and `b` fields for each document and returns both the raw score and the normalized score:

```javascript
db.vectors.aggregate( [
   {
      $project: {
         raw: { $similarityDotProduct: [ "$a", "$b" ] },
         normalized: {
            $similarityDotProduct: {
               vectors: [ "$a", "$b" ],
               score: true
            }
         }
      }
   }
] )
```

The operation returns the following results:

```javascript
{ _id: 1, raw: 14, normalized: 7.5 }
{ _id: 2, raw: 10, normalized: 5.5 }
{ _id: 3, raw: 32, normalized: 16.5 }
```

## Learn More

- :pipeline:`$vectorSearch`
- `aggregation-expressions`
