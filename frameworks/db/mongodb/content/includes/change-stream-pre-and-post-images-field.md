---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream-pre-and-post-images-field.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
