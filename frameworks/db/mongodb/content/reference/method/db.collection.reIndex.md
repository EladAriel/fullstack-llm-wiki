---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.reIndex.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# db.collection.reIndex() (mongosh method)

.. include:: /includes/fact-mongosh-shell-method-alt

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Behavior

For MongoDB 5.0 or later, :method:`db.collection.reIndex()` may only be run on `standalone` instances.

### Resource Locking

:method:`db.collection.reIndex()` obtains an exclusive (W) lock on the collection and blocks other operations on the collection until it completes.

For more information on locking in MongoDB, see `/faq/concurrency`.

> **Seealso:** `/indexes`
