---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/atlas-search-commands/access-control/create-access-control.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
