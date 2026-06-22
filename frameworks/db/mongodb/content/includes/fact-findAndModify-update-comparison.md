---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-findAndModify-update-comparison.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When updating a document, |operation| and the :method:`~db.collection.updateOne()` method operate differently:

- If multiple documents match the update criteria, for
|operation|, you can specify a `sort` to provide some measure of control on which document to update.

:method:`~db.collection.updateOne()` updates the first document that matches.

- By default, |operation| returns |return-object|. To
obtain the updated document, use the `new` option.

The :method:`~db.collection.updateOne()` method returns a :method:`WriteResult` object that contains the status of the operation.

To return the updated document, use the :method:`~db.collection.find()` method. However, other updates may have modified the document between your update and the document retrieval. Also, if the update modified only a single document but multiple documents matched, you will need to use additional logic to identify the updated document.

When modifying a single document, both |operation| and the :method:`~db.collection.updateOne()` method atomically update the document. See `/core/write-operations-atomicity` for more details about interactions and order of operations of these methods.
