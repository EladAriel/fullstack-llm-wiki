---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream-pre-and-post-images-introduction.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 6.0, you can use `change stream events <change-stream-output>` to output the version of a document before and after changes (the document pre- and post-images):

- The pre-image is the document before it was replaced, updated, or
deleted. There is no pre-image for an inserted document.

- The post-image is the document after it was inserted, replaced, or
updated. There is no post-image for a deleted document.

- Enable `changeStreamPreAndPostImages` for a collection using
:method:`db.createCollection()`, :dbcommand:`create`, or :dbcommand:`collMod`. For example, when using the `collMod` command:

```javascript
  db.runCommand( { 
     collMod: <collection>,
     changeStreamPreAndPostImages: { enabled: true }
  } )
```
