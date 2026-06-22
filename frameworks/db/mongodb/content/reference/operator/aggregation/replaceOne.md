---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/replaceOne.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $replaceOne  (expression operator)

## Definition

## Syntax

The :expression:`$replaceOne` operator has the following `operator expression syntax <agg-quick-ref-operator-expressions>`:

```javascript
{ $replaceOne: { input: <expression>, find: <expression>, replacement: <expression> } }
```

### Operator Fields

## Behavior

If no occurrences of `find <replaceOne-find>` are found in `input <replaceOne-input>`, :expression:`$replaceOne` evaluates to the input string.

The `input <replaceOne-input>`, `find <replaceOne-find>`, and `replacement <replaceOne-replacement>` expressions must evaluate to one of the following output types:

- A string
- `null`
- A regex for `find <replaceOne-find>` operations
Otherwise, :expression:`$replaceOne` fails with an error.

### `$replaceOne` and Null Values

If `input <replaceOne-input>` or `find <replaceOne-find>` refer to a field that is missing, they return `null`.

If any one of `input <replaceOne-input>`, `find <replaceOne-find>`, or `replacement <replaceOne-replacement>` evaluates to a `null`, the entire :expression:`$replaceOne` expression evaluates to `null`:

### $replaceOne and Collation

.. include:: /includes/collation-replace-example.rst

The following :expression:`$replaceOne` operation tries to find and replace the first instance of "Cafe" in the `name` field:

Because :expression:`$replaceOne` ignores the collation configured for this collection, the operation only matches the instance of "Cafe" in document `2`.

Operators that respect collation, such as :pipeline:`$match`, would match all three documents when performing a string comparison against "Cafe" due to this collection's collation strength of `1`.

### `$replaceOne` and Unicode Normalization

The :expression:`$replaceOne` aggregation expression does not perform any unicode normalization. This means that string matching for all `$replaceOne` expressions will consider the number of code points used to represent a character in unicode when attempting a match.

For example, the character `é` can be represented in unicode using either one code point or two:

Using :expression:`$replaceOne` with a `find <replaceOne-find>` string where the character `é` is represented in unicode with one code point will not match any instance of `é` that uses two code points in the `input <replaceOne-input>` string.

The following table shows whether a match occurs for a `find <replaceOne-find>` string of "café" when compared to `input <replaceOne-input>` strings where `é` is represented by either one code point or two. The `find <replaceOne-find>` string in this example uses one code point to represent the `é` character:

Because :expression:`$replaceOne` does not perform any unicode normalization, only the first string comparison matches, where both the `find <replaceOne-find>` and `input <replaceOne-input>` strings use one code point to represent `é`.

## Examples

Create an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "blue paint" },
   { _id: 2, item: "blue and green paint" },
   { _id: 3, item: "blue paint with blue paintbrush" },
   { _id: 4, item: "blue paint with green paintbrush" },
] )
```

### Replace Using a String

The following example replaces the first instance of "blue paint" in the `item` field with "red paint":

```javascript
db.inventory.aggregate([
   {
     $project:
      {
         item: { $replaceOne: { input: "$item", find: "blue paint", replacement: "red paint" } }
      }
   }
])
```

The operation returns the following results:

```javascript
{ _id: 1, item: "red paint" }
{ _id: 2, item: "blue and green paint" }
{ _id: 3, item: "red paint with blue paintbrush" }
{ _id: 4, item: "red paint with green paintbrush" }
```

Note that with document `3`, only the first matched instance of "blue paint" is replaced.

### Replace Using Regex

The following example replaces the first instance of "blue" as a whole word in the `item` field with "navy":

```javascript
db.inventory.aggregate([
   {
     $project:
      {
         item: { $replaceOne: { input: "$item", find: \\bblue\\b, replacement: "navy" } }
      }
   }
]);
```

The operation returns the following results:

```javascript
{ _id: 1, item: "navy paint" }
{ _id: 2, item: "navy and green paint" }
{ _id: 3, item: "navy paint with blue paintbrush" }
{ _id: 4, item: "navy paint with green paintbrush" }
```

Note that with document `3`, only the first matched instance of "blue" is replaced.
