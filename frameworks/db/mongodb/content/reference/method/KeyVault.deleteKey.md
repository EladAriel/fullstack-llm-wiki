---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/KeyVault.deleteKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# KeyVault.deleteKey() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Requires Configuring Client-Side Field Level Encryption on Database Connection

.. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

## Example

The following example is intended for rapid evaluation of client-side field level encryption. For specific examples of using :method:`KeyVault.deleteKey()` with each supported :abbr:`KMS (Key Management Service)` provider, see `field-level-encryption-data-key-delete`.

.. include:: /includes/csfle-connection-boilerplate-example.rst

Retrieve the :method:`KeyVault <getKeyVault()>` object and use the :method:`KeyVault.deleteKey()` method to delete the data encryption key with matching `UUID`:

```javascript
keyVault = encryptedClient.getKeyVault()
keyVault.deleteKey(UUID("b4b41b33-5c97-412e-a02b-743498346079"))
```

If successful, :method:`~KeyVault.deleteKey()` returns output similar to the following:

```json
{ "acknowledged" : true, "deletedCount" : 1 }
```

> **Seealso:** `field-level-encryption-data-key-delete`
