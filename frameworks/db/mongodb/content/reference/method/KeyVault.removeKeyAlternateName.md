---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/KeyVault.removeKeyAlternateName.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================================

# KeyVault.removeKeyAlternateName() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

:method:`~KeyVault.removeKeyAlternateName()` has the following syntax:

```none
keyVault = db.getMongo().getKeyVault()

keyVault.removeKeyAlternateName(
   UUID("<UUID string>"),
   "keyAltName"
)
```

## Behavior

### Requires Configuring Client-Side Field Level Encryption on Database Connection

.. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

## Example

The following example is intended for rapid evaluation of client-side field level encryption. For specific examples of using :method:`KeyVault.removeKeyAlternateName()` with each supported :abbr:`KMS (Key Management Service)` provider, see `field-level-encryption-data-key-manage`.

.. include:: /includes/csfle-connection-boilerplate-example.rst

Retrieve the :method:`keyVault <getKeyVault()>` object and use the :method:`KeyVault.removeKeyAlternateName()` method to remove the specified key alternate name from the data encryption key with matching `UUID`:

```javascript
keyVault = encryptedClient.getKeyVault()
keyVault.removeKeyAlternateName(UUID("b4b41b33-5c97-412e-a02b-743498346079"),"Other-Data-Encryption-Key")
```

If successful, :method:`~KeyVault.removeKeyAlternateName()` returns the data encryption key prior to updating the `keyAltName`.

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
        "ssn-encryption-key"
    ]
}
```
