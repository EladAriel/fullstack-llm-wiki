---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/anyElementTrue.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# $anyElementTrue (expression operator)

## Definition

## Behavior

.. include:: /includes/extracts/fact-agg-top-level-expressions-anyElementTrue.rst

.. include:: /includes/extracts/fact-agg-boolean-anyElementTrue.rst

## Example

Create an example collection named `survey` with the following documents:

```javascript
db.survey.insertMany( [
   { _id: 1, responses: [ true ] },
   { _id: 2, responses: [ true, false ] },
   { _id: 3, responses: [ ] },
   { _id: 4, responses: [ 1, true, "seven" ] },
   { _id: 5, responses: [ 0 ] },
   { _id: 6, responses: [ [ ] ] },
   { _id: 7, responses: [ [ 0 ] ] },
   { _id: 8, responses: [ [ false ] ] },
   { _id: 9, responses: [ null ] },
   { _id: 10, responses: [ undefined ] }
] )
```

The following operation uses the :expression:`$anyElementTrue` operator to determine if the `responses` array contains any value that evaluates to `true`:

In the results:

- Document with `_id: 1` is `true` because the element inside the
`responses` array evaluates as `true`.

- Documents with `_id: 2 and id: 4` are `true` because at least
one element inside the `responses` array evaluates as `true`.

- Documents with `_id: 6, id: 7, and id: 8` are `true`
because the `responses` array, which is the array that `$anyElementTrue` evaluated for the operation, contains a nested array, which `$anyElementTrue` always evaluates as `true`.
