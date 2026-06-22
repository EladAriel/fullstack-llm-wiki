---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/tsSecond.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $tsSecond  (expression operator)

## Definition

.. versionadded:: 5.1

.. include:: /includes/tsSecond-introduction.rst

:expression:`$tsSecond` syntax:

```none
{ $tsSecond: <expression> }
```

The `expression <aggregation-expressions>` must resolve to a `timestamp <document-bson-type-timestamp>`.

> **Seealso:** - `aggregation-expressions`
- `bson-types`
- :expression:`$tsIncrement`

## Behavior

:expression:`$tsSecond` returns:

- `Null` if the input `expression <aggregation-expressions>`
evaluates to `null` or refers to a field that is missing.

- An error if the input `expression <aggregation-expressions>` does
not evaluate to a `timestamp <document-bson-type-timestamp>`.

## Examples

### Obtain the Number of Seconds from a Timestamp Field

.. include:: /includes/stockSales-example-collection.rst

The following example uses :expression:`$tsSecond` in a :pipeline:`$project` pipeline stage to return the seconds from the stock sales `saleTimestamp` field:

```javascript
db.stockSales.aggregate( [
   {
      $project:
      {
         _id: 0, saleTimestamp: 1, saleSeconds: { $tsSecond: "$saleTimestamp" }
      }
   }
] )
```

Example output:

```javascript
{
  saleTimestamp: Timestamp({ t: 1622731060, i: 1 }),
  saleSeconds: Long("1622731060")
},
{
  saleTimestamp: Timestamp({ t: 1622731060, i: 2 }),
  saleSeconds: Long("1622731060")
},
{
  saleTimestamp: Timestamp({ t: 1714124193, i: 1 }),
  saleSeconds: Long("1714124193")
},
{
  saleTimestamp: Timestamp({ t: 1714124193, i: 2 }),
  saleSeconds: Long("1714124193")
},
{
  saleTimestamp: Timestamp({ t: 1714124193, i: 3 }),
  saleSeconds: Long("1714124193")
}
```

### Use `$tsSecond` in a Change Stream Cursor to Monitor Collection Changes

The example in this section uses :expression:`$tsSecond` in a `change stream cursor <changeStreams>` to monitor changes to a collection.

Create a `change stream cursor <changeStreams>` on a collection named `cakeSales` that you will see later in this section:

```javascript
cakeSalesCursor = db.cakeSales.watch( [
   {
      $addFields: {
         clusterTimeSeconds: { $tsSecond: "$clusterTime" }
      }
   }
] )
```

In the example, the:

- :method:`db.collection.watch()` method creates a :ref:`change stream
cursor <changeStreams>` for the `cakeSales` collection and stores the cursor in `cakeSalesCursor`.

- :pipeline:`$addFields` stage adds a field named `clusterTimeSeconds`
to `cakeSalesCursor`.

- `$clusterTime` is the timestamp from the :ref:`oplog
<replica-set-oplog>` entry for the `cakeSales` collection change. See `Command Response <command-response>`.

- :expression:`$tsSecond` returns the seconds from `$clusterTime`,
which is stored in `clusterTimeSeconds`.

.. include:: /includes/cakeSales-example-collection.rst

To monitor the `cakeSales` collection changes, use `cakeSalesCursor`. For example, to obtain the next document from `cakeSalesCursor`, use the :method:`~cursor.next()` method:

```javascript
cakeSalesCursor.next()
```

The following example output shows the `insert` details for the first document added to the `cakeSales` collection. The `clusterTimeSeconds` field contains the seconds from the `clusterTime` field.

```javascript
_id: {
  _data: '82613A4A51000000032B022C0100296E5A100495189B4131584C56AC8BA9D540799F23461E5F696400290004'
},
operationType: 'insert',
clusterTime: Timestamp({ t: 1631210065, i: 3 }),
fullDocument: {
  _id: 0,
  type: 'chocolate',
  orderDate: ISODate("2020-05-18T14:10:30.000Z"),
  state: 'CA',
  price: 13,
  quantity: 120
},
ns: { db: 'test', coll: 'cakeSales' },
documentKey: { _id: 0 },
clusterTimeSeconds: 1631210065
```
