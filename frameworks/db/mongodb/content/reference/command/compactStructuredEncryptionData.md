---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/compactStructuredEncryptionData.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================================

# compactStructuredEncryptionData (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
  {
    compactStructuredEncryptionData: <collection>,
    compactionTokens: {
       encryptedFieldPath: bindata,
       ...
    },
  }
)
```

## Command Fields

The command takes the following fields:

The :binary:`~bin.mongosh` provides a wrapper method :method:`db.collection.compactStructuredEncryptionData()`.

## Required Access

The built-in roles :authrole:`readWriteAnyDatabase` and :authrole:`dbOwner` provide :authaction:`compactStructuredEncryptionData` actions on resources.

## Example

See `metadata collection compaction <qe-metadata-compaction>` for an example.
