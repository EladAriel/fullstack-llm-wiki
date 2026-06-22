---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/similarityCosine.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# $similarityCosine (expression operator)

## Definition

.. versionadded:: 8.3

## Behavior

### `null` and Missing Values

If either argument resolves to `null` or refers to a missing field, :expression:`$similarityCosine` returns `null`.

### Zero-Magnitude Vectors

If either input vector has a magnitude of zero (that is, all elements are `0`), :expression:`$similarityCosine` returns `0`.

### Return Value

:expression:`$similarityCosine` returns a `double`. When `score` is `false` (the default), the result is the raw cosine similarity value in the range `[-1, 1]`:

- `1` indicates the vectors point in identical directions.
- `0` indicates the vectors are orthogonal.
- `-1` indicates the vectors point in opposite directions.
When `score` is `true`, the result is normalized to the range `[0, 1]` using the formula `(1 + cosine) / 2`.

### Errors

:expression:`$similarityCosine` returns an error in the following cases:

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

The following aggregation pipeline computes the cosine similarity between the `a` and `b` fields for each document and returns both the raw score and the normalized score:

```javascript
db.vectors.aggregate( [
   {
      $project: {
         raw: { $similarityCosine: [ "$a", "$b" ] },
         normalized: {
            $similarityCosine: {
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
{ _id: 1, raw: 1, normalized: 1 }
{ _id: 2, raw: 0.7142857142857143,
  normalized: 0.8571428571428571 }
{ _id: 3, raw: 0.9746318461970762,
  normalized: 0.9873159230985381 }
```

## Learn More

- :pipeline:`$vectorSearch`
- `aggregation-expressions`
