---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/setFeatureCompatibilityVersion.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# setFeatureCompatibilityVersion (database command)

## Definition

> **Warning:** Enabling backwards-incompatible features can complicate the
downgrade process since you must remove any persisted
backwards-incompatible features before you downgrade.
It is recommended that after upgrading, you allow your deployment to
run without enabling backwards-incompatible features for a burn-in period
to ensure the likelihood of downgrade is minimal. When you are confident
that the likelihood of downgrade is minimal, enable these features.

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

.. versionchanged:: 8.3

The command has the following syntax:

```javascript
db.adminCommand( 
   {
     setFeatureCompatibilityVersion: <version>,
     confirm: true,
     writeConcern: { wtimeout: <timeout> },
     dryRun: <boolean>
   } 
)
```

## Command Fields

The `setFeatureCompatibilityVersion` command takes the following fields:

### setFeatureCompatibilityVersion

Required

The possible values for `version` are:

### confirm

Required

.. versionadded:: 7.0

Set to `true` to confirm the feature compatibility change and allow the operation to proceed.

If you omit the `confirm` parameter or set `confirm` to a value other than `true`, the command fails and returns a warning about modifying the feature compatibility version.

### writeConcern

Optional

The `writeConcern` specifies the write concern `wc-wtimeout` value in milliseconds:

- The time period that the `primary` waits for
acknowledgment from the majority of the replica set members. If the acknowledgment is not received in the time period, the operation fails.

- Default is `60000` milliseconds. Use a longer time period if the
`secondary` members of the replica set have a delay that exceeds the `wc-wtimeout` default.

> **Note:** .. include:: /includes/list-run-command-targets.rst

### dryRun

Optional

If set to `true`, MongoDB simulates an upgrade or downgrade of the feature compatibility version. If the cluster contains incompatible data, the operation fails with an error.

.. versionadded:: 8.3

## Behavior

If you must downgrade the `feature compatibility version <view-fcv>` below 8.0, you must first run the `transitionToDedicatedConfigServer` command. For downgrade details, see `sharded-cluster-config-server-config-shards-downgrade`.

### Upgrade with Forward-Incompatible Data

If you try to upgrade the {+fcv+} of a cluster that contains forwards-incompatible data in the upgraded version, you receive a `CannotUpgrade` error. Forwards-incompatible data can refer to any data in your cluster that relies on a feature that was removed in the target version.

When this error occurs, either:

- Modify your cluster data to remove forwards-incompatible
features, then re-run the `setFeatureCompatibilityVersion` command with the upgraded version to set the {+fcv+} to the upgraded version.

- Run the `setFeatureCompatibilityVersion` command with the
original downgraded version to set the {+fcv+} back to the original version.

> **Important:**   Setting the {+fcv+} to the original version stops the
  upgrade procedure and changes the {+fcv+} back to the
  downgraded version. This procedure does not reset the
  cluster back to the state before the {+fcv+} upgrade
  began.
  If the {+fcv+} upgrade confirms that there is no
  forwards-incompatible data but otherwise stops or fails,
  any subsequent FCV downgrade attempts will also fail with
  an error message. You must complete the FCV upgrade before
  trying to downgrade the FCV.

### Downgrade with Backward-Incompatible Data

If you try to downgrade the {+fcv+} of a cluster that contains backwards-incompatible data in the downgraded version, you receive a `CannotDowngrade` error. Backwards-incompatible data can refer to any data in your cluster that relies on a feature that isn't available in the target version.

When this error occurs, either:

- Modify your cluster data to remove backwards-incompatible
features, then re-run the `setFeatureCompatibilityVersion` command with the downgraded version to set the {+fcv+} to the downgraded version.

- Run the `setFeatureCompatibilityVersion` command with the
original upgraded version to set the {+fcv+} back to the original version.

> **Important:**   Setting the {+fcv+} to the original version stops the
  downgrade procedure and changes the {+fcv+} back to the
  upgraded version. This procedure does not reset the cluster
  back to the state before the {+fcv+} downgrade began.
  If the {+fcv+} downgrade confirms that there is no
  backwards-incompatible data but otherwise stops or fails,
  any subsequent FCV upgrade attempts will also fail with
  an error message. You must complete the FCV downgrade before
  trying to upgrade the FCV.

### Downgrade Policy in MongoDB 8.3

Starting in 8.3, you can downgrade your deployment's {+fcv+} to the immediately previous minor version.

To learn more, see `8.3-downgrade`.

### Conflicts with Background Operations

Certain background operations may prevent execution of :dbcommand:`setFeatureCompatibilityVersion`. Use :dbcommand:`currentOp` to identify any ongoing operations.

### Sync Failures

If you trigger a :dbcommand:`setFeatureCompatibilityVersion` change during an initial sync, the sync may fail with an `OplogOperationUnsupported` error message when replaying entries on the `oplog` application phase. The sync following this attempt succeeds because the operation phase no longer replays the operation.

### Default Values

.. include:: /includes/list-table-featureCompatibilityVersion-defaults.rst

### Idempotency

This command must perform writes to an internal system collection. If for any reason the command does not complete successfully, you can safely retry the command as the operation is idempotent.

### {+c2c-product-name+} and User Write Blocking

.. include:: /includes/downgrade-for-user-write-blocking.rst

#. If you enabled cluster-to-cluster replication, disable it.

#. If you enabled user write blocking, disable it:

```javascript
   db.runCommand( { setUserWriteBlockMode: 1, global: false } )
```

#. Wait for the previous command to complete.

#. Downgrade the feature compatibility version using :dbcommand:`setFeatureCompatibilityVersion`.

For more information on {+c2c-full-product-name+}, see the [documentation]({+c2c-docs+})_.

### Feature Compatibility in Arbiters

.. include:: /includes/arbiter-fcv.rst

For example, an arbiter in a MongoDB 5.0 cluster, has an FCV value of 4.4.

## Examples

### Get FeatureCompatibilityVersion

To view the `featureCompatibilityVersion` for a :binary:`~bin.mongod` instance, run the :dbcommand:`getParameter` command on a :binary:`~bin.mongod` instance:

```javascript
db.adminCommand(
   {
      getParameter: 1,
      featureCompatibilityVersion: 1
   }
 )
```

The output resembles:

```javascript
{
  featureCompatibilityVersion: { version: '5.0' },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1660318752, i: 5 }),
    signature: {
      hash: Binary(Buffer.from("ce0cff3621e9b089fa6d8e9a1e1efc1a1ff15dab", "hex"), 0),
      keyId: Long("7129893797260951557")
    }
  },
  operationTime: Timestamp({ t: 1660318752, i: 5 })
}
```

> **Note:** The operation is undefined on the :binary:`~bin.mongos` instances.
On a sharded cluster that has access control enabled, you must
connect to the shard as a `shard local user <shard-local-users>`
to run the command.

### Set Feature Compatibility Version on MongoDB 8.0 Deployments

Enable 8.0 Backwards Incompatible Features `````````````````````````````````````````` To enable the `8.0 features that persist data incompatible with MongoDB 7.0 <8.0-downgrade-incompatible>`, set the feature compatibility to `"8.0"` on the MongoDB 8.0 deployment:

> **Note:** Run the :dbcommand:`setFeatureCompatibilityVersion` command against
the `admin` database.
.. include:: /includes/list-run-command-targets.rst

```javascript
db.adminCommand(
   {
      setFeatureCompatibilityVersion: "8.0",
      confirm: true
   }
)
```

Disable 8.0 Backwards Incompatible Features ```````````````````````````````````````````

To disable the `8.0 features that persist data incompatible with MongoDB 7.0 <8.0-downgrade-incompatible>`, set the feature compatibility to `"7.0"` on the MongoDB 8.0 deployment:

> **Note:** Run the :dbcommand:`setFeatureCompatibilityVersion` command against
the `admin` database.
.. include:: /includes/list-run-command-targets.rst
- `"7.0"` featureCompatibilityVersion is supported on MongoDB
  7.0 and MongoDB 8.0 deployments.

```javascript
db.adminCommand(
   {
      setFeatureCompatibilityVersion: "7.0",
      confirm: true
   }
)
```

If you run this command as part of the downgrade process from MongoDB 8.0 to MongoDB 7.0, you must also remove all persisted features that are `incompatible <8.0-downgrade-incompatible>` with 7.0. See the appropriate downgrade procedures.

### Set Feature Compatibility Version on MongoDB 7.0 Deployments

Enable 7.0 Backwards Incompatible Features ``````````````````````````````````````````

To enable the `7.0 features that persist data incompatible with MongoDB 6.0 <7.0-downgrade-incompatible>`, set the feature compatibility to `"7.0"` on the MongoDB 7.0 deployment:

> **Note:** Run the :dbcommand:`setFeatureCompatibilityVersion` command against
the `admin` database.
.. include:: /includes/list-run-command-targets.rst

```javascript
db.adminCommand(
   {
      setFeatureCompatibilityVersion: "7.0",
      confirm: true
   }
)
```

Disable 7.0 Backwards Incompatible Features ```````````````````````````````````````````

To disable the `7.0 features that persist data incompatible with MongoDB 6.0 <7.0-downgrade-incompatible>`, set the feature compatibility to `"6.0"` on the MongoDB 7.0 deployment:

> **Note:** Run the :dbcommand:`setFeatureCompatibilityVersion` command against
the `admin` database.
.. include:: /includes/list-run-command-targets.rst
- `"6.0"` featureCompatibilityVersion is supported on MongoDB
  6.0 and MongoDB 7.0 deployments only.

```javascript
db.adminCommand(
   {
      setFeatureCompatibilityVersion: "6.0",
      confirm: true
   }
)
```

If run as part of the downgrade process from MongoDB 7.0 to MongoDB 6.0, you must also remove all persisted features that are `incompatible <7.0-downgrade-incompatible>` with 6.0. See the appropriate downgrade procedures.

### Set Write Concern Timeout

The following example sets the optional write concern `wc-wtimeout` field to 5000 (5 seconds).

> **Note:** Run the :dbcommand:`setFeatureCompatibilityVersion` command against
the `admin` database.
.. include:: /includes/list-run-command-targets.rst

```javascript
db.adminCommand( {
   setFeatureCompatibilityVersion: "5.0",
   writeConcern: { wtimeout: 5000 }
} )
```

## Troubleshooting

If you experience startup issues after setting your feature compatibility version, contact {+mdb-support+} for assistance.
