---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ClientEncryption.decrypt.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================

# ClientEncryption.decrypt() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`ClientEncryption.decrypt` has the following syntax:

```javascript
clientEncryption = db.getMongo().getClientEncryption()

clientEncryption.decrypt(encryptedValue)
```

The `encryptedValue` must be a :bsontype:`binary data <Binary>` object with [subtype 6](https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/subtype6.rst) created using client-side field level encryption.

## Behavior

Read operations issued from a database connection :method:`configured <Mongo()>` with access to the correct Key Management Service (KMS) and Key Vault can automatically decrypt field values encrypted using :method:`ClientEncryption.encrypt()`. Clients only need to use :method:`~ClientEncryption.decrypt()` to decrypt :bsontype:`Binary` subtype 6 values not stored within a document field.

### Enable Client-Side Field Level Encryption on Database Connection

.. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

## Example

The following example uses a locally managed KMS for the client-side field level encryption configuration.

### Example Results

If successful, :method:`~ClientEncryption.decrypt()` returns the decrypted value:

```javascript
"123-45-6789" 
```

## Learn More

For complete documentation on initiating MongoDB connections with client-side field level encryption enabled, see :method:`Mongo()`.
