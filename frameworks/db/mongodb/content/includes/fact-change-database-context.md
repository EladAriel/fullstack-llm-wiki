---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-change-database-context.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Use the `use <database-name>` helper in :binary:`~bin.mongosh`, or the following :method:`db.getSiblingDB()` method in an interactive :binary:`~bin.mongosh` session or in :binary:`~bin.mongosh` shell scripts to change the `db` object:

```javascript
db = db.getSiblingDB('<database-name>')
```
