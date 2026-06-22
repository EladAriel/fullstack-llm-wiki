---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/map.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $map (expression operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :expression:`$map` expression has the following syntax:

```javascript
{ 
   $map: {
      input: <expression>,
      as: <string>,
      arrayIndexAs: <string>,
      in: <expression>
   }
}
```

For more information on expressions, see `aggregation-expressions`.

## Examples

### Add to Each Element of an Array

.. include:: /includes/sample-data-usage.rst

The following aggregation operation uses :expression:`$map` with the :expression:`$add` expression to add `10` to each element in the `location.geo.coordinates` array:

### Truncate Each Array Element

The following aggregation operation uses :expression:`$map` to :expression:`truncate <$trunc>` each element in the `location.geo.coordinates` array to its integer:

### Apply Arithmetic Operators to Each Array Element

The following aggregation operation uses the :pipeline:`$addFields` stage to add a new `genreScores` field. The operation uses :expression:`$map` to apply :expression:`$multiply` and :expression:`$add` to each element in the `genres` array, computing a score based on the character count of each genre name:

### Access the Index of Each Item in an Array

The `genres` field in the `movies` collection contains an array of genre names for each movie.

The following example uses `arrayIndexAs`. The `myIndex` variable has the index of each genre in the `genres` array. The example returns documents with these fields:

- Movie title.
- Genre name.
- Position of the genre in the `genres` array in the `rank`
field.

- `isPrimary` boolean that is `true` for the first genre in
the array, and `false` for the other genres.

### Use `$$IDX` to Access the Index

.. include:: /includes/IDX-use.rst

The following example returns the same documents as the previous example in `map-index-example`, but uses `$$IDX` instead of `arrayIndexAs`:

## Learn More

To learn more about expressions used in the previous examples, see:

- :expression:`$add`
- :expression:`$multiply`
- :expression:`$trunc`
- :expression:`$strLenCP`
