---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/fullDocument-update.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

This field only appears if you configured the change stream with `fullDocument` set to `updateLookup`. When you configure the change stream with `updateLookup`, the field represents the current majority-committed version of the document modified by the update operation. The document may differ from the changes described in `updateDescription <|idref|-updateDescription>` if any other majority-committed operations have modified the document between the original update operation and the full document lookup.

For more information, see `Lookup Full Document for Update Operations <change-streams-updateLookup>`.
