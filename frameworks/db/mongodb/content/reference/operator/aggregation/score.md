---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/score.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $score (aggregation)

.. versionadded:: 8.2

## Definition

## Syntax

The stage has the following syntax:

```javascript
{ 
  $score: { 
    score: <expression>,
    scoreDetails: <boolean>,
    normalization: "none|sigmoid|minMaxScaler",
    weight: <expression>
  } 
}
```

## Fields

`$score` takes the following fields:

## Behavior

The output documents from a :pipeline:`$score` are the same as the input documents, but includes additional computed score as metadata.

If you specify multiple :pipeline:`$score` stages in the pipeline, the last :pipeline:`$score` stage in the pipeline overrides the score metadata from previous :pipeline:`$score` stages.

### scoreDetails

If you set `scoreDetails` to `true`, `$score` creates a `scoreDetails` metadata field for each document. The `scoreDetails` field contains information about the final ranking.

> **Note:** When you set `scoreDetails` to `true`, `$score` sets the
`scoreDetails` metadata field for each document but does not automatically
output the `scoreDetails` metafield.
To view the `scoreDetails` metadata field, you must either:
- use a :pipeline:`$project` stage after `$score` to project the
  `scoreDetails` field
- use a :pipeline:`$addFields` stage after `$score` to add the
  `scoreDetails` field to your pipeline output

The `scoreDetails` field contains the following subfields:

.. include:: /includes/fact-scoreDetails-output-format.rst

For example, the following code blocks shows the `scoreDetails` field for a `$score` operation with an `$add` expression:

```js
{
 _id: ObjectId('55f5a192d4bede9ac365b257'),
 scoreDetails: {
   value: 0.5,
   description: 'the score calculated from multiplying a weight in the range [0,1] with either a normalized or nonnormalized value:',
   rawScore: 145,
   normalization: 'sigmoid',
   weight: 0.5,
   expression: '{ string: { $add: [ 'field', 'myField' ] } }',
   details: []
 }
},
```
