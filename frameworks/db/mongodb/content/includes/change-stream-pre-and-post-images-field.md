---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream-pre-and-post-images-field.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional.

.. include:: /includes/change-stream-pre-and-post-images-introduction.rst

`changeStreamPreAndPostImages` has the following syntax:

```javascript
changeStreamPreAndPostImages: {
   enabled: <boolean>
}
```

To enable change stream pre- and post-images for the collection, set `enabled` to `true`.

For complete examples with the change stream output, see `db.collection.watch-change-streams-pre-and-post-images-example`.
