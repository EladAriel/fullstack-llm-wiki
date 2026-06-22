---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/atlas-search-commands/access-control/list-access-control.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If your deployment enforces access control, the user running |method-name| must have the :authaction:`listSearchIndexes` privilege action on the database or collection:

```javascript
{
   resource: {
      db : <database>,
      collection: <collection>
   },
   actions: [ "listSearchIndexes" ]
}
```

The built-in :authrole:`read` role provides the the `listSearchIndexes` privilege. The following example grants the `read` role on the `qa` database:

```javascript
db.grantRolesToUser(
   "<user>",
   [ { role: "read", db: "qa" } ]
)
```
