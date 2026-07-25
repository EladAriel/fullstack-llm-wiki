---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.1-regex-document-schema-validation.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.1, if a collection has `schema validation <schema-validation-query-expression>` rules that contain invalid :query:`$regex options <$regex>` the server:

- Prevents all insert and update operations until the schema validation
rules containing the invalid regex pattern are modified with the :dbcommand:`collMod` command.

- Writes a warning error to the :binary:`~bin.mongod` log file.
