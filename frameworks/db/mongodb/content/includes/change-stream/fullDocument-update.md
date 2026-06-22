---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/fullDocument-update.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This field only appears if you configured the change stream with `fullDocument` set to `updateLookup`. When you configure the change stream with `updateLookup`, the field represents the current majority-committed version of the document modified by the update operation. The document may differ from the changes described in `updateDescription <|idref|-updateDescription>` if any other majority-committed operations have modified the document between the original update operation and the full document lookup.

For more information, see `Lookup Full Document for Update Operations <change-streams-updateLookup>`.
