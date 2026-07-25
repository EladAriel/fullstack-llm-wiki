---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream-pre-and-post-images-full-document-before-change.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 6.0, you can use the new `fullDocumentBeforeChange` field and set it to:

- `"whenAvailable"` to output the document pre-image, if available,
before the document was replaced, updated, or deleted.

- `"required"` to output the document pre-image before the document
was replaced, updated, or deleted. Raises an error if the pre-image is not available.

- `"off"` to suppress the document pre-image. `"off"` is the
default.
