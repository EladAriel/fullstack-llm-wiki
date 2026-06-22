---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/regexMatch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# $regexMatch (expression operator)

## Definition

## Syntax

The :expression:`$regexMatch` operator has the following syntax:

```javascript
{ $regexMatch: { input: <expression> , regex: <expression>, options: <expression> } }
```

### Returns

The operator returns a boolean:

- `true` if a match exists.
- `false` if a match doesn't exist.
> **Seealso:** - :expression:`$regexFind`
- :expression:`$regexFindAll`

## Behavior

### PCRE Library

.. include:: /includes/fact-6.1-pcre2.rst

### $regexMatch and Collation

.. include:: /includes/regex-operator-collation.rst

```javascript
db.restaurants.aggregate( [
   {
      $addFields: { 
         resultObject: { $regexMatch: { input: "$category", regex: /cafe/ } }
      }
   }
] )

db.restaurants.aggregate( [
   {
      $addFields: {
         resultObject: { $regexMatch: { input: "$category", regex: /cafe/ } }
      }
   }
], 
   { collation: { locale: "fr", strength: 1 } } // Ignored in the $regexMatch
)
```

.. include:: /includes/regex-collation-example-output.rst

To perform a case-insensitive regex pattern matching, use the `regexMatch-example-i-options` instead. See `regexMatch-example-i-options` for an example.

## Examples

### `$regexMatch` and Its Options

To illustrate the behavior of the :expression:`$regexMatch` operator as discussed in this example, create a sample collection `products` with the following documents:

```javascript
db.products.insertMany([
   { _id: 1, description: "Single LINE description." },
   { _id: 2, description: "First lines\nsecond line" },
   { _id: 3, description: "Many spaces before     line" },
   { _id: 4, description: "Multiple\nline descriptions" },
   { _id: 5, description: "anchors, links and hyperlinks" },
   { _id: 6, description: "métier work vocation" }
])
```

By default, :expression:`$regexMatch` performs a case-sensitive match. For example, the following aggregation performs a case-sensitive :expression:`$regexMatch` on the `description` field. The regex pattern `/line/` does not specify any grouping:

```javascript
db.products.aggregate([
   { $addFields: { result: { $regexMatch: { input: "$description", regex: /line/ } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "result" : false }
{ "_id" : 2, "description" : "First lines\nsecond line", "result" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "result" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "result" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "result" : false }
{ "_id" : 6, "description" : "métier work vocation", "result" : false }
```

The following regex pattern `/lin(e|k)/` specifies a grouping `(e|k)` in the pattern:

```javascript
db.products.aggregate([
   { $addFields: { result: { $regexMatch: { input: "$description", regex: /lin(e|k)/ } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "result" : false }
{ "_id" : 2, "description" : "First lines\nsecond line", "result" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "result" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "result" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "result" : true }
{ "_id" : 6, "description" : "métier work vocation", "result" : false }
```

`i` Option ````````````

.. include:: /includes/extracts/agg-regex-options-one-place-only.rst

To perform case-insensitive pattern matching, include the `i <regexMatch-options>` option as part of the `regex <regexMatch-regex>` field or in the `options <regexMatch-options>` field:

```javascript
// Specify i as part of the regex field
{ $regexMatch: { input: "$description", regex: /line/i } }

// Specify i in the options field
{ $regexMatch: { input: "$description", regex: /line/, options: "i" } }
{ $regexMatch: { input: "$description", regex: "line", options: "i" } }
```

For example, the following aggregation performs a case-insensitive :expression:`$regexMatch` on the `description` field. The regex pattern `/line/` does not specify any grouping:

```javascript
db.products.aggregate([
   { $addFields: { result: { $regexMatch: { input: "$description", regex: /line/i } } } }
])
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "result" : true }
{ "_id" : 2, "description" : "First lines\nsecond line", "result" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "result" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "result" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "result" : false }
{ "_id" : 6, "description" : "métier work vocation", "result" : false }
```

`m` Option ````````````

.. include:: /includes/extracts/agg-regex-options-one-place-only.rst

To match the specified anchors (e.g. `^`, `$`) for each line of a multiline string, include the `m <regexMatch-options>` option as part of the `regex <regexMatch-regex>` field or in the `options <regexMatch-options>` field:

```javascript
// Specify m as part of the regex field
{ $regexMatch: { input: "$description", regex: /line/m } }

// Specify m in the options field
{ $regexMatch: { input: "$description", regex: /line/, options: "m" } }
{ $regexMatch: { input: "$description", regex: "line", options: "m" } }
```

The following example includes both the `i` and the `m` options to match lines starting with either the letter `s` or `S` for multiline strings:

```javascript
db.products.aggregate([
   { $addFields: { result: { $regexMatch: { input: "$description", regex: /^s/im } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "result" : true }
{ "_id" : 2, "description" : "First lines\nsecond line", "result" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "result" : false }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "result" : false }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "result" : false }
{ "_id" : 6, "description" : "métier work vocation", "result" : false }
```

`x` Option ````````````

.. include:: /includes/extracts/agg-regex-options-one-place-only.rst

To ignore all unescaped white space characters and comments (denoted by the un-escaped hash `#` character and the next new-line character) in the pattern, include the `s <regexMatch-options>` option in the `options <regexMatch-options>` field:

```javascript
// Specify x in the options field
{ $regexMatch: { input: "$description", regex: /line/, options: "x" } }
{ $regexMatch: { input: "$description", regex: "line", options: "x" } }
```

The following example includes the `x` option to skip unescaped white spaces and comments:

```javascript
db.products.aggregate([
   { $addFields: { returns: { $regexMatch: { input: "$description", regex: /lin(e|k) # matches line or link/, options:"x" } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returns" : false }
{ "_id" : 2, "description" : "First lines\nsecond line", "returns" : true }
{ "_id" : 3, "description" : "Many spaces before     line", "returns" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returns" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returns" : true }
{ "_id" : 6, "description" : "métier work vocation", "returns" : false }
```

`s` Option ````````````

.. include:: /includes/extracts/agg-regex-options-one-place-only.rst

To allow the dot character (i.e. `.`) in the pattern to match all characters including the new line character, include the `s <regexMatch-options>` option in the `options <regexMatch-options>` field:

```javascript
// Specify s in the options field
{ $regexMatch: { input: "$description", regex: /m.*line/, options: "s" } }
{ $regexMatch: { input: "$description", regex: "m.*line", options: "s" } }
```

The following example includes the `s` option to allow the dot character (i.e. .) to match all characters including new line as well as the `i` option to perform a case-insensitive match:

```javascript
db.products.aggregate([
   { $addFields: { returns: { $regexMatch: { input: "$description", regex:/m.*line/, options: "si"  } } } }
])
```

The operation returns the following:

```javascript
{ "_id" : 1, "description" : "Single LINE description.", "returns" : false }
{ "_id" : 2, "description" : "First lines\nsecond line", "returns" : false }
{ "_id" : 3, "description" : "Many spaces before     line", "returns" : true }
{ "_id" : 4, "description" : "Multiple\nline descriptions", "returns" : true }
{ "_id" : 5, "description" : "anchors, links and hyperlinks", "returns" : false }
{ "_id" : 6, "description" : "métier work vocation", "returns" : false }
```

### Use `$regexMatch` to Check Email Address

Create a sample collection `feedback` with the following documents:

```javascript
db.feedback.insertMany([
   { "_id" : 1, comment: "Hi, I'm just reading about MongoDB -- aunt.arc.tica@example.com"  },
   { "_id" : 2, comment: "I wanted to concatenate a string" },
   { "_id" : 3, comment: "How do I convert a date to string? Contact me at either cam@mongodb.com or c.dia@mongodb.com" },
   { "_id" : 4, comment: "It's just me. I'm testing.  fred@MongoDB.com" }
])
```

The following aggregation uses the :expression:`$regexMatch` to check if the `comment` field contains an email address with `@mongodb.com` and categorize the feedback as `Employee` or `External`.

```javascript
db.feedback.aggregate( [ 
    { $addFields: { 
       "category": { $cond: { if:  { $regexMatch: { input: "$comment", regex: /[a-z0-9_.+-]+@mongodb.com/i } },
                              then: "Employee",
                              else: "External" } }
    } },
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "comment" : "Hi, I'm just reading about MongoDB -- aunt.arc.tica@example.com", "category" : "External" }
{ "_id" : 2, "comment" : "I wanted to concatenate a string", "category" : "External" }
{ "_id" : 3, "comment" : "How do I convert a date to string? Contact me at either cam@mongodb.com or c.dia@mongodb.com", "category" : "Employee" }
{ "_id" : 4, "comment" : "It's just me. I'm testing.  fred@MongoDB.com", "category" : "Employee" }
```
