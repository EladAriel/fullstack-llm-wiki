---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream-pre-and-post-images-change-events.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 6.0, you see a `fullDocumentBeforeChange` document with the fields before the document was changed (or deleted) if you perform these steps:

#. Enable the new `changeStreamPreAndPostImages` field for a collection using :method:`db.createCollection()`, :dbcommand:`create`, or :dbcommand:`collMod`.

#. Set `fullDocumentBeforeChange` to `"required"` or `"whenAvailable"` in :method:`db.collection.watch()`.

Example `fullDocumentBeforeChange` document in the change stream output:

```json
"fullDocumentBeforeChange" : {
   "_id" : ObjectId("599af247bb69cd89961c986d"), 
   "userName" : "alice123",
   "name" : "Alice Smith"
}
```

For complete examples with the change stream output, see `db.collection.watch-change-streams-pre-and-post-images-example`.
