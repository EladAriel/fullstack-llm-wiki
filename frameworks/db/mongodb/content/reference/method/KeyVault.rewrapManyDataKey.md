---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/KeyVault.rewrapManyDataKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# KeyVault.rewrapManyDataKey() (mongosh method)

> **Warning:** Before you rotate your {+dek-long+}s, ensure you create
a backup of your {+key-vault-long+}. If you lose access to your
{+dek-long+}s, you will lose all your encrypted data.
To learn how to create a backup of a collection,
see `<manual-tutorial-backup-and-restore>`.

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`KeyVault.rewrapManyDataKey` has the following syntax:

```javascript
let keyVault = db.getMongo().getKeyVault()

keyVault.rewrapManyDataKey(
 <filter>,
 <options>
)
```

.. include:: /includes/in-use-encryption/admonition-csfle-key-rotation.txt

## Behavior

This operation is not atomic and should not be run in parallel with other key management operations.

### Requires Configuring Client-Side Field Level Encryption on Database Connection

.. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

## Example

These examples allow you to rapidly evaluate client-side field level encryption. For specific examples using each supported :abbr:`KMS (Key Management Service)` provider, see `field-level-encryption-data-key-manage`.

.. include:: /includes/csfle-connection-boilerplate-example.rst

Retrieve the :method:`KeyVault <getKeyVault()>` object and use the :method:`KeyVault.rewrapManyDataKey` method to rewrap the existing keys in a new `masterKey`. If no new `masterKey` is given, each data key retains its respective current `masterKey`.

### Rewrap Data Keys with the Current masterKey

The following example shows how you can rewrap each data key with its respective current `masterKey`:

```javascript
let keyVault = mongo.getKeyVault()

keyVault.rewrapManyDataKey()
```

### Rewrap Data Keys with a New masterKey

The following example shows how you can rewrap each data key with a new `masterKey`:

```javascript
let keyVault = mongo.getKeyVault()

keyVault.rewrapManyDataKey({}, {
  provider: 'aws',
  masterKey: {
    region: 'us-east-2',
    key: 'arn:aws:kms:us-east-2:...'
  }
})
```

### Rewrap Data Keys That Have Not Been Rewrapped Recently

The following example shows how to rewrap data keys that have not been rewrapped in the previous thirty days.

```javascript
let keyVault = mongo.getKeyVault()

const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

keyVault.rewrapManyDataKey({ updateDate: { $lt: thirtyDaysAgo } });
```

### Output

:method:`KeyVault.rewrapManyDataKey()` returns a `BulkWriteResult` object detailing how many data keys were affected:

```json
{
  bulkWriteResult: BulkWriteResult {
    result: {
      ok: 1,
      writeErrors: [],
      writeConcernErrors: [],
      insertedIds: [],
      nInserted: 0,
      nUpserted: 0,
      nMatched: 3,
      nModified: 3,
      nRemoved: 0,
      upserted: [],
      opTime: { ts: Timestamp({ t: 1655840760, i: 3 }), t: 23 }
    }
  }
}
```
