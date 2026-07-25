---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/indexOfBytes.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================================

# $indexOfBytes (expression operator)

## Definition

## Behavior

- If `<string expression>` is null, :expression:`$indexOfBytes` returns `null`.
- If :expression:`$indexOfBytes` is called on a field that doesn't exist in the document, :expression:`$indexOfBytes` returns `null`.
- If `<string expression>` is not a string and not null, :expression:`$indexOfBytes` returns an error.
- If `<substring expression>` is null, :expression:`$indexOfBytes` returns an error.
- If `<start>` or `<end>` is a negative number, :expression:`$indexOfBytes` returns an error.
- If `<start>` is a number greater than `<end>`, :expression:`$indexOfBytes` returns `-1`.
- If `<start>` is a number greater than the byte length of the string, :expression:`$indexOfBytes` returns `-1`.
- If `<start>` or `<end>` is given a value that is not an integer, :expression:`$indexOfBytes` returns an error.
- If the `<substring expression>` is found multiple times within the `<string expression>`, then :expression:`$indexOfBytes` returns the index of the first `<substring expression>` found.
Some short examples to highlight different behavior:

## Examples

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "foo" },
   { _id: 2, item: "fóofoo" },
   { _id: 3, item: "the foo bar" },
   { _id: 4, item: "hello world fóo" },
   { _id: 5, item: null },
   { _id: 6, amount: 3 }
] )
```

The following operation uses the :expression:`$indexOfBytes` operator to retrieve the indexes at which the string `foo` is located in each item:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            byteLocation: { $indexOfBytes: [ "$item", "foo" ] },
          }
      }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, byteLocation: "0" }
{ _id: 2, byteLocation: "4" }
{ _id: 3, byteLocation: "4" }
{ _id: 4, byteLocation: "-1" }
{ _id: 5, byteLocation: null }
{ _id: 6, byteLocation: null }
```

> **Seealso:** - :expression:`$indexOfCP`
- :expression:`$indexOfArray`
