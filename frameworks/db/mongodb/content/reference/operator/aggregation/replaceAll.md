---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/replaceAll.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $replaceAll  (expression operator)

## Definition

## Syntax

The :expression:`$replaceAll` operator has the following `operator expression syntax <agg-quick-ref-operator-expressions>`:

```javascript
{ $replaceAll: { input: <expression>, find: <expression>, replacement: <expression> } }
```

### Operator Fields

## Behavior

The `input <replaceAll-input>`, `find <replaceAll-find>`, and `replacement <replaceAll-replacement>` expressions must evaluate to a string or a `null` (or regex for `find <replaceAll-find>`), or :expression:`$replaceAll` fails with an error.

### `$replaceAll` and Null Values

If `input <replaceAll-input>` or `find <replaceAll-find>` refer to a field that is missing, they return `null`.

If any one of `input <replaceAll-input>`, `find <replaceAll-find>`, or `replacement <replaceAll-replacement>` evaluates to a `null`, the entire :expression:`$replaceAll` expression evaluates to `null`:

### $replaceAll and Collation

.. include:: /includes/collation-replace-example.rst

The following `$replaceAll` operation tries to find and replace all instances of "Cafe" in the `name` field:

Because :expression:`$replaceAll` ignores the collation configured for this collection, the operation only matches the instance of "Cafe" in document `2`:

```javascript
{ _id: 1, name: "cafe", resultObject: "cafe" }
{ _id: 2, name: "Cafe", resultObject: "CAFE" }
{ _id: 3, name: "café", resultObject: "café" }
```

Operators that respect collation, such as :pipeline:`$match`, would match all three documents when performing a string comparison against "Cafe" due to this collection's collation strength of `1`.

### `$replaceAll` and Unicode Normalization

The :expression:`$replaceAll` aggregation expression does not perform any unicode normalization. This means that string matching for all `$replaceAll` expressions will consider the number of code points used to represent a character in unicode when attempting a match.

For example, the character `é` can be represented in unicode using either one code point or two:

Using :expression:`$replaceAll` with a `find <replaceAll-find>` string where the character `é` is represented in unicode with one code point will not match any instance of `é` that uses two code points in the `input <replaceAll-input>` string.

The following table shows whether a match occurs for a `find <replaceAll-find>` string of "café" when compared to `input <replaceAll-input>` strings where `é` is represented by either one code point or two. The `find <replaceAll-find>` string in this example uses one code point to represent the `é` character:

Because :expression:`$replaceAll` does not perform any unicode normalization, only the first string comparison matches, where both the `find <replaceAll-find>` and `input <replaceAll-input>` strings use one code point to represent `é`.

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

The following example replaces each instance of "blue paint" in the `item` field with "red paint":

```javascript
db.inventory.aggregate([
   {
     $project:
      {
         item: { $replaceAll: { input: "$item", find: "blue paint", replacement: "red paint" } }
      }
   }
])
```

The operation returns the following results:

```javascript
{ _id: 1, item: "red paint" }
{ _id: 2, item: "blue and green paint" }
{ _id: 3, item: "red paint with red paintbrush" }
{ _id: 4, item: "red paint with green paintbrush" }
```

### Replace Using Regex

The following example uses a regex pattern `\\bblue paint\\b` to replace each instance matching "blue paint" as a whole phrase in the `item` field with "red paint":

```javascript
db.inventory.aggregate([  
   {  
     $project:
      {  
         item: { $replaceAll: { input: "$item", find: \\bblue paint\\b, replacement: "red paint" } }  
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

In this case, "blue paint" is replaced only when it appears as a whole phrase, due to the use of regex word boundaries (`\b`), and not when it is a substring within a larger word.
