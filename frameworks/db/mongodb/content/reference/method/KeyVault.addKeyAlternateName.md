---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/KeyVault.addKeyAlternateName.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# KeyVault.addKeyAlternateName() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

:method:`~KeyVault.addKeyAlternateName()` has the following syntax:

```none
keyVault = db.getMongo().getKeyVault()

keyVault.addKeyAlternateName(
   UUID("<UUID string>"),
   "keyAlternateName"
)
```

## Behavior

### Requires Configuring Client-Side Field Level Encryption on Database Connection

.. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

## Example

The following example is intended for rapid evaluation of client-side field level encryption. For specific examples of using :method:`KeyVault.addKeyAlternateName()` with each supported :abbr:`KMS (Key Management Service)` provider, see `field-level-encryption-data-key-manage`.

.. include:: /includes/csfle-connection-boilerplate-example.rst

Retrieve the :method:`KeyVault <getKeyVault()>` object and use the :method:`KeyVault.addKeyAlternateName()` method to add a new key alternate name to the data encryption key with matching `UUID`. The specified key alternate name must be unique:

```javascript
keyVault = encryptedClient.getKeyVault()
keyVault.addKeyAlternateName(UUID("b4b41b33-5c97-412e-a02b-743498346079"),"Other-Data-Encryption-Key")
```

If successful, :method:`~KeyVault.addKeyAlternateName()` returns the previous version of data encryption key document:

```json
{
    "_id" : UUID("b4b41b33-5c97-412e-a02b-743498346079"),
    "keyMaterial" : BinData(0,"PXRsLOAYxhzTS/mFQAI8486da7BwZgqA91UI7NKz/T/AjB0uJZxTvhvmQQsKbCJYsWVS/cp5Rqy/FUX2zZwxJOJmI3rosPhzV0OI5y1cuXhAlLWlj03CnTcOSRzE/YIrsCjMB0/NyiZ7MRWUYzLAEQnE30d947XCiiHIb8a0kt2SD0so8vZvSuP2n0Vtz4NYqnzF0CkhZSWFa2e2yA=="),
    "creationDate" : ISODate("2019-08-12T21:21:30.569Z"),
    "updateDate" : ISODate("2019-08-12T21:21:30.569Z"),
    "status" : 0,
    "version" : Long(0),
    "masterKey" : {
        "provider" : "local"
    },
    "keyAltNames" : [
    ]
}
```

To view the current version of the data encryption key document, use :method:`KeyVault.getKey() specifying the id` of the returned document or :method:`KeyVault.getKeyByAltName()` specifying one of the `keyAltNames`.

> **Seealso:** `field-level-encryption-data-key-manage`
