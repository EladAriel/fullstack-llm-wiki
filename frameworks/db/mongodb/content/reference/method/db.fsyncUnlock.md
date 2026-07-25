---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.fsyncUnlock.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================

# db.fsyncUnlock() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

### Compatibility with WiredTiger

.. include:: /includes/extracts/wt-fsync-lock-compatibility.rst

## Example

Consider a situation where :method:`db.fsyncLock()` has been issued two times. The following :method:`db.fsyncUnlock()` operation reduces the locks taken by :method:`db.fsyncLock()` by 1:

```javascript
db.fsyncUnlock()
```

The operation returns the following document:

```javascript
{ "info" : "fsyncUnlock completed", "lockCount" : Long(1), "ok" : 1 }
```

As the `lockCount` is greater than 0, the :binary:`~bin.mongod` instance is locked against writes. To unlock the instance for writes, run :method:`db.fsyncLock()` again:

```javascript
db.fsyncUnlock()
```

The operation returns the following document:

```javascript
{ "info" : "fsyncUnlock completed", "lockCount" : Long(0), "ok" : 1 }
```

The :program:`mongod` instance is unlocked for writes.
