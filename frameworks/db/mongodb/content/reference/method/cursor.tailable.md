---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.tailable.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# cursor.tailable() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

A tailable cursor performs a collection scan over a `capped collection <manual-capped-collection>`. It remains open even after reaching the end of the collection. Applications can continue to iterate the tailable cursor as new data is inserted into the collection.

If `awaitData` is `true`, when the cursor reaches the end of the capped collection, :program:`mongod` blocks the query thread for the timeout interval and waits for new data to arrive. When new data is inserted into the capped collection, `mongod` signals the blocked thread to wake and return the next batch to the client.

See `tailable-cursors-landing-page`.
