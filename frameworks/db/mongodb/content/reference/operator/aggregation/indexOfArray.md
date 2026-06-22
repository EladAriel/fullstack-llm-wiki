---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/indexOfArray.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# $indexOfArray (expression operator)

## Definition

## Behavior

If the `<search expression>` is found multiple times within the `<array expression>`, then :expression:`$indexOfArray` returns the index of the first `<search expression>` from the starting index position.

:expression:`$indexOfArray` returns `null`:

- If `<array expression>` is null, or
- If `<array expression>` refers to a non-existing field in the input
document.

:expression:`$indexOfArray` returns an error:

- If `<array expression>` is not an array and not null, or
- If `<start>` or `<end>` is a negative integer (or a value that
can be represented as a negative integer, like -5.0).

:expression:`$indexOfArray` returns `-1`:

- If the <search expression> is not found in the array, or
- If `<start>` is a number greater than `<end>`, or
- If `<start>` is a number greater than the length of the array.
## Example

The example uses this `inventory` collection:

```javascript
db.inventory.insertMany( [
   { _id: 0, items: [ "one", "two", "three" ] },
   { _id: 1, items: [ 1, 2, 3 ] },
   { _id: 2, items: [ 1, 2, 3, 2 ] },
   { _id: 3, items: [ null, null, 2 ] },
   { _id: 4, items: [ 2, null, null, 2 ] },
   { _id: 5, items: null },
   { _id: 6, amount: 3 }
] )
```

The following example uses :expression:`$indexOfArray` to find `2` in the `items` array:

```javascript
db.inventory.aggregate( [ {
   $project: {
      index: { $indexOfArray: [ "$items", 2 ] }
   }
} ] )
```

The example returns:

- The first array index for the value `2` in each `items` array, if
found. Array indexes start at `0`.

- `-1` for the index if `2` is not in the `items` array.
- `null` for the index if `items` is not an array or `items` does
not exist.

Example output:

```javascript
[
   { _id: 0, index: -1 },
   { _id: 1, index: 1 },
   { _id: 2, index: 1 },
   { _id: 3, index: 2 },
   { _id: 4, index: 0 },
   { _id: 5, index: null },
   { _id: 6, index: null }
]
```

> **Seealso:** - :expression:`$indexOfBytes`
- :expression:`$indexOfCP`
- :expression:`$in`
