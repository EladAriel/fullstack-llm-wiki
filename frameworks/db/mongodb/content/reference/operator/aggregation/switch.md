---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/switch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $switch (expression operator)

## Definition

## Behavior

The various case statements do not need to be mutually exclusive. :expression:`$switch` executes the first branch it finds which evaluates to `true`. If none of the branches evaluates to true, :expression:`$switch` executes the `default` option.

The following conditions cause :expression:`$switch` to fail with an error:

- The `branches` field is missing or is not an array with at least
one entry.

- An object in the `branches` array does not contain a `case`
field.

- An object in the `branches` array does not contain a `then`
field.

- An object in the `branches` array contains a field other than
`case` or `then`.

- No `default` is specified and no `case` evaluates to `true`.
## Example

A collection named `grades` contains the following documents:

```javascript
{ "_id" : 1, "name" : "Susan Wilkes", "scores" : [ 87, 86, 78 ] }
{ "_id" : 2, "name" : "Bob Hanna", "scores" : [ 71, 64, 81 ] }
{ "_id" : 3, "name" : "James Torrelio", "scores" : [ 91, 84, 97 ] }
```

The following aggregation operation uses :expression:`$switch` to display a particular message based on each student's average score.

```javascript
db.grades.aggregate( [
  {
    $project: 
      {
        "name" : 1,
        "summary" : 
        {
          $switch:
            {
              branches: [
                {
                  case: { $gte : [ { $avg : "$scores" }, 90 ] },
                  then: "Doing great!"
                },
                {
                  case: { $and : [ { $gte : [ { $avg : "$scores" }, 80 ] }, 
                                   { $lt : [ { $avg : "$scores" }, 90 ] } ] },
                  then: "Doing pretty well."
                },
                {
                  case: { $lt : [ { $avg : "$scores" }, 80 ] },
                  then: "Needs improvement."
                }
              ],
              default: "No scores found."
            }
         }
      }
   }
] )
```

The operation returns the following:

```javascript
{ "_id" : 1, "name" : "Susan Wilkes", "summary" : "Doing pretty well." }
{ "_id" : 2, "name" : "Bob Hanna", "summary" : "Needs improvement." }
{ "_id" : 3, "name" : "James Torrelio", "summary" : "Doing great!" }
```

> **Seealso:** :expression:`$cond`
