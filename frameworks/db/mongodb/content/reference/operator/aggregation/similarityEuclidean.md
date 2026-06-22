---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/similarityEuclidean.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# $similarityEuclidean (expression operator)

## Definition

.. versionadded:: 8.3

## Behavior

### `null` and Missing Values

If either argument resolves to `null` or refers to a missing field, :expression:`$similarityEuclidean` returns `null`.

### Return Value

:expression:`$similarityEuclidean` returns a `double`. When `score` is `false` (the default), the result is the raw Euclidean distance, which is always greater than or equal to `0`. A distance of `0` means the vectors are identical. Larger values indicate greater dissimilarity.

When `score` is `true`, the result is normalized to the range `(0, 1]` using the formula `1 / (1 + distance)`:

- `1` indicates the vectors are identical (distance is `0`).
- Values approaching `0` indicate greater dissimilarity.
### Errors

:expression:`$similarityEuclidean` returns an error in the following cases:

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

The following aggregation pipeline computes the Euclidean distance between the `a` and `b` fields for each document and returns both the raw distance and the normalized score:

```javascript
db.vectors.aggregate( [
   {
      $project: {
         raw: { $similarityEuclidean: [ "$a", "$b" ] },
         normalized: {
            $similarityEuclidean: {
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
{ _id: 1, raw: 0, normalized: 1 }
{ _id: 2, raw: 2.8284271247461903,
  normalized: 0.2612038749637415 }
{ _id: 3, raw: 5.196152422706632,
  normalized: 0.16139702886038895 }
```

## Learn More

- :pipeline:`$vectorSearch`
- `aggregation-expressions`
