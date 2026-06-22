---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/indexOfCP.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $indexOfCP (expression operator)

## Definition

## Behavior

If the `<substring expression>` is found multiple times within the `<string expression>`, then :expression:`$indexOfCP` returns the index of the first `<substring expression>` found from the starting index position.

:expression:`$indexOfCP` returns `null`:

- If `<string expression>` is null, or
- If `<string expression>` refers to a non-existing field in the
input document.

:expression:`$indexOfCP` returns an error:

- If `<string expression>` is not a string and not null, or
- If `<substring expression>` is null or is not a string or refers to
a nonexistent field in the input document, or

- If `<start>` or `<end>` is a negative integer (or a value that
can be represented as a negative integer, like -5.0).

:expression:`$indexOfCP` returns `-1`:

- If the substring is not found in the `<string expression>`, or
- If `<start>` is a number greater than `<end>`, or
- If `<start>` is a number greater than the byte length of the string.
## Examples

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "foo" }
   { _id: 2, item: "fóofoo" }
   { _id: 3, item: "the foo bar" }
   { _id: 4, item: "hello world fóo" }
   { _id: 5, item: null }
   { _id: 6, amount: 3 }
] )
```

The following operation uses the :expression:`$indexOfCP` operator to return the code point index at which the string `foo` is located in each `item` string:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            cpLocation: { $indexOfCP: [ "$item", "foo" ] },
          }
      }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, cpLocation: "0" }
{ _id: 2, cpLocation: "3" }
{ _id: 3, cpLocation: "4" }
{ _id: 4, cpLocation: "-1" }
{ _id: 5, cpLocation: null }
{ _id: 6, cpLocation: null }
```

> **Seealso:** - :expression:`$indexOfBytes`
- :expression:`$indexOfArray`
