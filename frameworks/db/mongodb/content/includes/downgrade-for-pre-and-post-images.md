---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/downgrade-for-pre-and-post-images.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 6.0, if you are using document pre- and post-images for `change streams <change-stream-output>`, you must disable `changeStreamPreAndPostImages <collMod-change-stream-pre-and-post-images>` for each collection using the :dbcommand:`collMod` command before you can downgrade to an earlier MongoDB version.
