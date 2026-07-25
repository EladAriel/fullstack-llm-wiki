---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-error-and-log-validation-action-backwards-incompatible.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If you use an `errorAndLog` validation action on a collection, MongoDB cannot downgrade until you drop the collection, or if you change the validation action for the collection to one supported in older versions. To change the validation action on a collection, use the :dbcommand:`collMod` command.
