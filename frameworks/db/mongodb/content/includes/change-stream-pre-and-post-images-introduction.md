---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream-pre-and-post-images-introduction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
