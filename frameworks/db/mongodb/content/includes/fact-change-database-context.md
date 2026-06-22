---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-change-database-context.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Use the `use <database-name>` helper in :binary:`~bin.mongosh`, or the following :method:`db.getSiblingDB()` method in an interactive :binary:`~bin.mongosh` session or in :binary:`~bin.mongosh` shell scripts to change the `db` object:

```javascript
db = db.getSiblingDB('<database-name>')
```
