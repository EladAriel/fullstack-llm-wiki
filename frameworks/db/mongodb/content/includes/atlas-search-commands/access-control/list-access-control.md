---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/atlas-search-commands/access-control/list-access-control.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
