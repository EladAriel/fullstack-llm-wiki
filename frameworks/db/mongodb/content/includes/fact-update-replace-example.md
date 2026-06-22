---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-update-replace-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When replacing a document, the replacement document must consist of only field/value pairs. The replacement document cannot include `update operators <update-operators-top-level>` expressions.

The replacement document can have different fields from the original document. In the replacement document, you can omit the `_id field since the id field is immutable. However, if you do include the id` field, it must have the same value as the current value.

The following example replaces the first document from the `inventory` collection where `item: "paper"`:
