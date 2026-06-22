---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-error-and-log-validation-action-backwards-incompatible.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you use an `errorAndLog` validation action on a collection, MongoDB cannot downgrade until you drop the collection, or if you change the validation action for the collection to one supported in older versions. To change the validation action on a collection, use the :dbcommand:`collMod` command.
