---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ClientEncryption.encrypt.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# ClientEncryption.encrypt() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
clientEncryption = db.getMongo().getClientEncryption()

clientEncryption.encrypt(
  keyId,
  value,
  algorithm or encOptions,
)
```

## Behavior

.. include:: /includes/create-an-encrypted-db-conn.rst

### Unsupported BSON Types

You cannot use :method:`~ClientEncryption.encrypt()` to encrypt values with the following BSON types:

- `minKey`
- `maxKey`
- `null`
- `undefined`
If encrypting a field using `AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic`, :method:`~ClientEncryption.encrypt()` does not support the following BSON types:

- `double`
- `decimal128`
- `bool`
- `object`
- `array`
## Examples

### Client-Side Field Level Encryption

The following example uses a locally managed KMS for the client-side field level encryption configuration.

Example Results ``````````````` If successful, :method:`~ClientEncryption.encrypt` returns the encrypted value:

```javascript
BinData(6,"AmTi2H3xaEk8u9+jlFNaLLkC3Q/+kmwDbbWrq+h9nuv9W+u7A5a0UnpULBNZH+Q21fAztPpU09wpKPrju9dKfpN1Afpj1/ZhFcH6LYZOWSBBOAuUNjPLxMNSYOOuITuuYWo=")
```

For complete documentation on initiating MongoDB connections with client-side field level encryption enabled, see :method:`Mongo()`.

### Queryable Encryption

The following example uses a locally managed KMS for the Queryable Encryption configuration.

Example Results ```````````````

If successful, :method:`~ClientEncryption.encrypt` returns the encrypted value:

```javascript
Binary(Buffer.from("05b100000005640020000000005ab3581a43e39a8e855b1ac87013e841735c09d19ae86535eea718dd56122ba50573002000000000703d2cba9832d90436c6c92eb232aa5b968cdcd7a3138570bc87ef0a9eb3a0e905630020000000009cb61df010b1bb54670a5ad979f25f4c48889059dfd8920782cf03dd27d1a50b05650020000000003f5acea703ea357d3eea4c6a5b19139a580089341424a247839fd4d5cf0d312a12636d00040000000000000000", "hex"), 6)
```

## Learn More

For complete documentation on initiating MongoDB connections with client-side field level encryption enabled, see :method:`Mongo()`.
