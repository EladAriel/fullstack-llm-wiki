---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/bottom.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $bottom (accumulator operator)

## Definition

> **Note:** This page describes the `$bottom` accumulator operator. For the `$bottom`
expression operator, see `$bottom (expression operator) <bottom_expression_operator>`.

## Syntax

```none
{
   $bottom:
      {
         sortBy: { <field1>: <sort order>, <field2>: <sort order> ... },
         output: <expression>
      }
}
```

## Behavior

### Null and Missing Values

Consider the following aggregation that returns the bottom document from a group of scores:

- `$bottom` does not filter out null values.
- `$bottom` converts missing values to null.
```javascript
db.aggregate( [
   {
      $documents: [
         { playerId: "PlayerA", gameId: "G1", score: 1 },
         { playerId: "PlayerB", gameId: "G1", score: 2 },
         { playerId: "PlayerC", gameId: "G1", score: 3 },
         { playerId: "PlayerD", gameId: "G1"},
         { playerId: "PlayerE", gameId: "G1", score: null }
      ]
   },
   {
      $group:
      {  
         _id: "$gameId",
         playerId:
            { 
               $bottom:
                  {    
                     output: [ "$playerId", "$score" ],
                     sortBy: { "score": -1 }
                  }
            }
      }
   }
] )
```

In this example:

- :pipeline:`$documents` creates the literal documents that contain
player scores.

- :pipeline:`$group` groups the documents by `gameId`. This
example has only one `gameId`, `G1`.

- `PlayerD` has a missing score and `PlayerE` has a
null `score`. These values are both considered as null.

- The `playerId` and `score` fields are specified as
`output : ["$playerId"," $score"]` and returned as array values.

- Specify the sort order with `sortBy: { "score": -1 }`.
- `PlayerD` and `PlayerE` tied for the bottom element. `PlayerD`
is returned as the bottom `score`.

- To have more deterministic tie breaking behavior for multiple null
values, add more fields to `sortBy`.

```javascript
[
   {
      _id: 'G1',
      playerId: [ 'PlayerD', null ]
   }
]
```

## Restrictions

### Window Function and Aggregation Expression Support

`$bottom` is not supported as a `aggregation expression <aggregation-expressions>`.

`$bottom` is supported as a :pipeline:`window operator <$setWindowFields>`.

### Memory Limit Considerations

Aggregation pipelines which call `$bottom` are subject to the `100 MB limit <agg-memory-restrictions>`. If this limit is exceeded for an individual group, the aggregation fails with an error.

## Examples

Consider a `gamescores` collection with the following documents:

```javascript
db.gamescores.insertMany([
   { playerId: "PlayerA", gameId: "G1", score: 31 },
   { playerId: "PlayerB", gameId: "G1", score: 33 },
   { playerId: "PlayerC", gameId: "G1", score: 99 },
   { playerId: "PlayerD", gameId: "G1", score: 1 },
   { playerId: "PlayerA", gameId: "G2", score: 10 },
   { playerId: "PlayerB", gameId: "G2", score: 14 },
   { playerId: "PlayerC", gameId: "G2", score: 66 },
   { playerId: "PlayerD", gameId: "G2", score: 80 }
])
```

### Find the Bottom `Score`

You can use the `$bottom` accumulator to find the bottom score in a single game.

```javascript
db.gamescores.aggregate( [
   {
      $match : { gameId : "G1" }
   },
   {
      $group:
         {
            _id: "$gameId",
            playerId:
               {
                  $bottom:
                  {
                     output: [ "$playerId", "$score" ],
                     sortBy: { "score": -1 }
                  }
               }
         }
   }
] )
```

The example pipeline:

- Uses :pipeline:`$match` to filter the results on a single `gameId`.
In this case, `G1`.

- Uses :pipeline:`$group` to group the results by `gameId`. In this
case, `G1`.

- Specifies the fields that are output for `$bottom` with
`output : ["$playerId"," $score"]`.

- Uses `sortBy: { "score": -1 }` to sort the scores in descending order.
- Uses `$bottom` to return the bottom score for the game.
The operation returns the following results:

```javascript
[ { _id: 'G1', playerId: [ 'PlayerD', 1 ] } ]
```

### Finding the Bottom `Score` Across Multiple Games

You can use the `$bottom` accumulator to find the bottom `score` in each game.

```javascript
db.gamescores.aggregate( [
      {
         $group:
         { _id: "$gameId", playerId:
            {
               $bottom:
                  {
                     output: [ "$playerId", "$score" ],
                     sortBy: { "score": -1 }
                  }
            }
         }
      }
] )
```

The example pipeline:

- Uses `$group` to group the results by `gameId`.
- Uses `$bottom` to return the bottom `score` for each game.
- Specifies the fields that are output for `$bottom` with
`output : ["$playerId", "$score"]`.

- Uses `sortBy: { "score": -1 }` to sort the scores in descending order.
The operation returns the following results:

```javascript
[
   { _id: 'G2', playerId: [ 'PlayerA', 10 ] },
   { _id: 'G1', playerId: [ 'PlayerD', 1 ] }
]
```
