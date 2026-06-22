---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.1-regex-document-schema-validation.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.1, if a collection has `schema validation <schema-validation-query-expression>` rules that contain invalid :query:`$regex options <$regex>` the server:

- Prevents all insert and update operations until the schema validation
rules containing the invalid regex pattern are modified with the :dbcommand:`collMod` command.

- Writes a warning error to the :binary:`~bin.mongod` log file.
