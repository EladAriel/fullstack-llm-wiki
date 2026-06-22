---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.reshardCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# sh.reshardCollection() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Considerations

.. include:: /includes/sharding/reshard-build-indexes-consideration.rst

### Reshard Limitations

.. include:: /includes/fact-reshard-limitations.rst

## Resharding Process

.. include:: /includes/reshard-collection-introduction.rst

### Initialization Phase

.. include:: /includes/reshard-collection-initialization.rst

### Clone Phase

.. include:: /includes/reshard-collection-clone.rst

### Index Phase

.. include:: /includes/reshard-collection-index.rst

### Apply and Catch-up Phase

.. include:: /includes/reshard-collection-apply-and-catchup.rst

> **Note:** If required, you can manually force the resharding operation to
complete by issuing the :method:`sh.commitReshardCollection()`
method. This is useful if the current time estimate to complete the
resharding operation is an acceptable duration for your collection
to block writes. The :method:`sh.commitReshardCollection()` method
blocks writes early and forces the resharding operation to
complete. During the time period where writes are blocked your
application experiences an increase in latency.

### Commit Phase

.. include:: /includes/reshard-collection-commit.rst

> **Note:** Once the resharding process reaches the commit phase, the process
cannot be ended with :method:`sh.abortReshardCollection()`.

## Examples

### Reshard a Collection

The following example reshards the `sales.orders` collection with the new shard key `{ order_id: 1 }`:

```javascript
sh.reshardCollection( "sales.orders", { order_id: 1 } )
```

Example output:

```javascript
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp(1, 1624887954),
    signature: {
      hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
      keyId: 0
    }
  },
  operationTime: Timestamp(1, 1624887947)
}
```

### Reshard a Collection to the same Shard Key

In order to reshard to the same shard key, set `forceRedistribution <forceRedistribution-option>` to `true`. The following example reshards the `sales.orders` collection to the same shard key `{ order_id: 1 }` and redistributes data.

```javascript
sh.reshardCollection( 
  "sales.orders", 
  { order_id: 1 }, 
  { forceRedistribution: true } 
)
```

Example output:

```javascript
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1733502241, i: 20 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1733502241, i: 20 })
}
```

For details, see `resharding-a-collection-back-to-same-key`.

### Reshard a Collection with Zones

Reshard a collection with zones when you need to adjust the distribution of data across the shards in your cluster to meet changing requirements or to improve performance.

In the following example, the `test.scores` collection resides on `shard0` and `shard1`. The current shard key is `{ _id: 1}`.

## Learn More

- `sharding-resharding`
