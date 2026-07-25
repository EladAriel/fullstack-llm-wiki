---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ClientEncryption.encryptExpression.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================================================

# ClientEncryption.encryptExpression() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
clientEncryption = db.getMongo().getClientEncryption()

clientEncryption.encryptExpression(
   keyId,
   expression,
   encOptions
)
```

## Behavior

.. include:: /includes/create-an-encrypted-db-conn.rst

## Examples

```javascript
clientEncryption.encryptExpression(
   UUID("64e2d87d-f168-493c-bbdf-a394535a2cb9"),
   {
      $and: [{ val: { $gt: Int32('100') } }, { val: { $lt: Int32('150') } }]
   },
   {
      algorithm: 'range',
      queryType: 'range',
      rangeOptions: { min: Int32('0'), max: Int32('200') },
      contentionFactor: 8
   })
```

If successful, `ClientEncryption.encryptExpression` returns the encrypted query result.

## Learn More

For complete documentation on initiating MongoDB connections with {+csfle+} or {+qe+} enabled, see :method:`Mongo()`.
