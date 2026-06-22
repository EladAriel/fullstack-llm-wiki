---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/function.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $function (expression operator)

## Definition

## Syntax

The :expression:`$function` operator has the following syntax:

```javascript
{ 
  $function: {
    body: <code>,
    args: <array expression>,
    lang: "js"
  }
}
```

## Considerations

### Schema Validation Restriction

You cannot use :expression:`$function` as part of a `schema validation <schema-validation-query-expression>` query predicate.

### Javascript Enablement

To use :expression:`$function`, you must have server-side scripting enabled (default).

If you do not use :expression:`$function` (or :group:`$accumulator`, :query:`$where`, or :dbcommand:`mapReduce`), disable server-side scripting:

- For a :binary:`~bin.mongod` instance, see
:setting:`security.javascriptEnabled` configuration option or :option:`--noscripting <mongod --noscripting>` command-line option.

- For a :binary:`~bin.mongos` instance, see
:setting:`security.javascriptEnabled` configuration option or the :option:`--noscripting <mongos --noscripting>` command-line option.

| In earlier versions, MongoDB does not allow JavaScript execution on :binary:`~bin.mongos` instances.

See also `security-checklist-javascript`.

### Alternative to `$where`

The query operator :query:`$where` can also be used to specify JavaScript expression. However:

- The :query:`$expr` operator allows the use of
`aggregation expressions <aggregation-expressions>` within the query language.

- The :expression:`$function` and :group:`$accumulator` allows users to define
custom aggregation expressions in JavaScript if the provided pipeline operators cannot fulfill your application's needs.

Given the available aggregation operators:

- The use of :query:`$expr` with aggregation operators that do not use
JavaScript (i.e. non-:expression:`$function` and non-:group:`$accumulator` operators) is faster than :query:`$where` because it does not execute JavaScript and should be preferred if possible.

- However, if you must create custom expressions,
:expression:`$function` is preferred over :query:`$where`.

### Unsupported Array and String Functions

.. include:: /includes/fact-6.0-js-engine-change.rst

## Examples

### Example 1: Usage Example

Create a sample collection named `players` with the following documents:

```javascript
db.players.insertMany([
   { _id: 1, name: "Miss Cheevous",  scores: [ 10, 5, 10 ] },
   { _id: 2, name: "Miss Ann Thrope", scores: [ 10, 10, 10 ] },
   { _id: 3, name: "Mrs. Eppie Delta ", scores: [ 9, 8, 8 ] }
])
```

The following aggregation operation uses :pipeline:`$addFields` to add new fields to each document:

- `isFound` whose value is determined by the custom
:expression:`$function` expression that checks whether the MD5 hash of the name is equal to a specified hash.

- `message` whose value is determined by the custom
:expression:`$function` expression that format a string message using a template.

```javascript
db.players.aggregate( [
   { $addFields:
      {
        isFound:
            { $function:
               {
                  body: function(name) { 
                     return hex_md5(name) == "15b0a220baa16331e8d80e15367677ad"
                  },
                  args: [ "$name" ],
                  lang: "js"
               }
            },
         message: 
            { $function:
               {
                  body: function(name, scores) {
                     let total = Array.sum(scores);
                     return `Hello ${name}.  Your total score is ${total}.`
                  },
                  args: [ "$name", "$scores"],
                  lang: "js"
               }
            }
       }
    }
] )
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "name" : "Miss Cheevous", "scores" : [ 10, 5, 10 ], "isFound" : false, "message" : "Hello Miss Cheevous.  Your total score is 25." }
{ "_id" : 2, "name" : "Miss Ann Thrope", "scores" : [ 10, 10, 10 ], "isFound" : true, "message" : "Hello Miss Ann Thrope.  Your total score is 30." }
{ "_id" : 3, "name" : "Mrs. Eppie Delta ", "scores" : [ 9, 8, 8 ], "isFound" : false, "message" : "Hello Mrs. Eppie Delta .  Your total score is 25." }
```

> **Tip:** Starting in MongoDB 8.3, you can use :expression:`$hexHash`
as a native aggregation alternative to `hex_md5`.
`$hexHash` does not require server-side JavaScript and
supports the SHA-256 and XXH64 algorithms in addition to MD5.
Note that `$hexHash` returns an uppercase hexadecimal string,
while `hex_md5` returns lowercase. MD5 is a legacy algorithm
and is disabled in FIPS mode.

### Example 2: Alternative to `$where`

> **Note:** The :query:`$expr` operator allows the use of
`aggregation expressions <aggregation-expressions>` within the
query language. And the :expression:`$function` and :group:`$accumulator`
allows users to define custom aggregation expressions in JavaScript if the
provided pipeline operators cannot fulfill your application's needs.
Given the available aggregation operators:
- The use of :query:`$expr` with aggregation operators that do not
  use JavaScript (i.e. non-:expression:`$function` and
  non-:group:`$accumulator` operators) is faster than
  :query:`$where` because it does not execute JavaScript and should
  be preferred if possible.
- However, if you must create custom expressions,
  :expression:`$function` is preferred over :query:`$where`.

As an alternative to a query that uses the :query:`$where` operator, you can use :query:`$expr` and :expression:`$function`. For example, consider the following :query:`$where` example.

```javascript
db.players.find( { $where: function() { 
   return (hex_md5(this.name) == "15b0a220baa16331e8d80e15367677ad") 
} } );
```

The :method:`db.collection.find()` operation returns the following document:

```javascript
{ "_id" : 2, "name" : "Miss Ann Thrope", "scores" : [ 10, 10, 10 ] }
```

The example can be expressed using :query:`$expr` and :expression:`$function`:

```javascript
db.players.find( {$expr: { $function: {
      body: function(name) { return hex_md5(name) == "15b0a220baa16331e8d80e15367677ad"; },
      args: [ "$name" ],
      lang: "js"
} } } )
```
