---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/collection-level-access-control.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================================

# Collection-Level Access Control in Self-Managed Deployments

Collection-level access control allows administrators to grant users privileges that are scoped to specific collections.

Administrators can implement collection-level access control through `user-defined roles <user-defined-roles>`. By creating a role with `privileges <privileges>` that are scoped to a specific collection in a particular database, administrators can provision users with roles that grant privileges on a collection level.

## Privileges and Scope

A privilege consists of `actions <security-user-actions>` and the `resources <resource-document>` upon which the actions are permissible; i.e. the resources define the scope of the actions for that privilege.

By specifying both the database and the collection in the `resource document <resource-specific-db-collection>` for a privilege, administrator can limit the privilege actions just to a specific collection in a specific database. Each privilege action in a role can be scoped to a different collection.

For example, a user defined role can contain the following privileges:

```javascript
privileges: [
  { resource: { db: "products", collection: "inventory" }, actions: [ "find", "update", "insert" ] },
  { resource: { db: "products", collection: "orders" },  actions: [ "find" ] }
]
```

The first privilege scopes its actions to the `inventory` collection of the `products` database. The second privilege scopes its actions to the `orders` collection of the `products` database.

As a best practice, avoid assigning `createCollection` privileges to users who don't have read privileges on the collection.

## Additional Information

For more information on user-defined roles and MongoDB authorization model, see `/core/authorization`. For a tutorial on creating user-defined roles, see `/tutorial/manage-users-and-roles`.
