---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/atlas-search-commands/access-control/create-access-control.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If your deployment enforces access control, the user running |method-name| must have the :authaction:`createSearchIndexes` privilege action on the database or collection:

```javascript
{
   resource: {
      db : <database>,
      collection: <collection>
   },
   actions: [ "createSearchIndexes" ]
}
```

The built-in :authrole:`readWrite` role provides the `createSearchIndexes` privilege. The following example grants `accountUser01` the `readWrite` role on the `products` database:

```javascript
db.grantRolesToUser(
   "accountUser01",
   [ { role: "readWrite", db: "products" } ]
)
```
