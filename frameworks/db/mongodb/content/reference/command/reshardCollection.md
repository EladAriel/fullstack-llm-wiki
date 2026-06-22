---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/reshardCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# reshardCollection (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

.. include:: /includes/reshardCollection-syntax.rst

## Command Fields

The command takes the following fields:

## Considerations

.. include:: /includes/sharding/reshard-build-indexes-consideration.rst

### Reshard Limitations

.. include:: /includes/fact-reshard-limitations.rst

## Resharding Process

.. include:: /includes/reshard-collection-introduction.rst

### Initialization Phase

During the initialization phase, the resharding coordinator determines the new data distribution for the sharded collection.

### Clone Phase

.. include:: /includes/reshard-collection-clone.rst

### Index Phase

.. include:: /includes/reshard-collection-index.rst

### Apply and Catch-up Phase

.. include:: /includes/reshard-collection-apply-and-catchup.rst

> **Note:** If desired, you can manually force the resharding operation to
complete by issuing the :dbcommand:`commitReshardCollection`
command. This is useful if the current time estimate to complete
the resharding operation is an acceptable duration for your
collection to block writes. The
:dbcommand:`commitReshardCollection` command blocks writes early
and forces the resharding operation to complete. During the time
period where writes are blocked your application experiences an
increase in latency.

### Commit Phase

.. include:: /includes/reshard-collection-commit.rst

> **Note:** Once the resharding process reaches the commit phase, the process
cannot be ended with :dbcommand:`abortReshardCollection`.

## Examples

### Reshard a Collection

The following example reshards the `sales.orders` collection with the new shard key `{ order_id: 1 }`:

```javascript
db.adminCommand({
  reshardCollection: "sales.orders",
  key: { order_id: 1 }
})
```

Output:

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

> **Seealso:** `sharding-resharding`

### Redistribute Data to New Shards

Starting in MongoDB 8.0, you can reshard a collection on the same key, which can be used to redistribute data onto new shards.

After adding a shard to the cluster, you use the `reshardCollection` command with the `forceRedistribution` option to redistribute data across the cluster:

```javascript
db.adminCommand({
    reshardCollection: "accounts.invoices",
    key: { store_id: "hashed" },
    forceRedistribution: true
})
```

### Redistribute Data to Different Zones

Starting in MongoDB 8.0, you can use the `reshardCollection` command to move data into new zones without changing the shard key.

The following command redistributes data for the `accounts.sales` collection using the same shard key, moving data to the shards associated with zones `zone04` and `zone05`:

```javascript
db.adminCommand({
    reshardCollection: "accounts.sales",
    key: { region_id: "hashed" },
    forceRedistribution: true,
    zones: [
        {
            zone: "zone04",
            min: { region_id: MinKey() },
            max: { region_id: 10 }
        },
        {
            zone: "zone05",
            min: { region_id: 10 },
            max: { region_id: MaxKey() }
        }
    ]
})
```

## Learn More

- `sharding-resharding`
