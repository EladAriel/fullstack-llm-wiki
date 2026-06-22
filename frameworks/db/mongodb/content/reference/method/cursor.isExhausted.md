---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.isExhausted.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# cursor.isExhausted() (mongosh method)

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Tailable Cursors

You can use `isExhausted()` with a `tailable cursor <tailable-cursors-landing-page>`. A tailable cursor stays open even if no documents remain in the current batch. Other cursors are automatically closed when no documents remain.

### Change Streams

You cannot use `isExhausted()` with `change streams <changeStreams>`. Instead, to examine if:

- documents remain in a change stream cursor, use
:method:`cursor.tryNext()`.

- a change stream cursor is closed, use :method:`cursor.isClosed()`.
For change stream examples, see `Watch Example <db.watch-example>` and `Change Stream Images Example <db.collection.watch-change-streams-pre-and-post-images-example>`.

## Examples

This section contains examples that use a cursor to read documents from a collection with temperature readings from a weather sensor. You'll see examples of `isExhausted()`.
