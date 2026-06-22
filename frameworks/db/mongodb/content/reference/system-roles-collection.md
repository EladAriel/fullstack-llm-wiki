---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/system-roles-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================================

# `system.roles` Collection in Self-Managed Deployments

The `system.roles` collection in the `admin` database stores the user-defined roles. To create and manage these user-defined roles, MongoDB provides `role management commands <role-management-commands>`.

## `system.roles` Schema

The documents in the `system.roles` collection have the following schema:

```javascript
{
  _id: <system-defined id>,
  role: "<role name>",
  db: "<database>",
  privileges:
      [
          {
              resource: { <resource> },
              actions: [ "<action>", ... ]
          },
          ...
      ],
  roles:
      [
          { role: "<role name>", db: "<database>" },
          ...
      ]
}
```

A `system.roles` document has the following fields:

## Examples

Consider the following sample documents found in `system.roles` collection of the `admin` database.

### A User-Defined Role Specifies Privileges

The following is a sample document for a user-defined role `appUser` defined for the `myApp` database:

```javascript
{
  _id: "myApp.appUser",
  role: "appUser",
  db: "myApp",
  privileges: [
       { resource: { db: "myApp" , collection: "" },
         actions: [ "find", "createCollection", "dbStats", "collStats" ] },
       { resource: { db: "myApp", collection: "logs" },
         actions: [ "insert" ] },
       { resource: { db: "myApp", collection: "data" },
         actions: [ "insert", "update", "remove", "compact" ] },
       { resource: { db: "myApp", collection: "system.js" },
         actions: [ "find" ] },
  ],
  roles: []
}
```

The `privileges` array lists the five privileges that the `appUser` role specifies:

- The first privilege permits its actions ( `"find"`,
`"createCollection"`, `"dbStats"`, `"collStats"`) on all the collections in the `myApp` database excluding its system collections. See `resource-specific-db`.

- The next two privileges permits additional actions on specific
collections, `logs` and `data`, in the `myApp` database. See `resource-specific-db-collection`.

- The last privilege permits actions on one :doc:`system
collections </reference/system-collections>` in the `myApp` database. While the first privilege gives database-wide permission for the `find` action, the action does not apply to `myApp`'s system collections. To give access to a system collection, a privilege must explicitly specify the collection. See `/reference/resource-document`.

As indicated by the empty `roles` array, `appUser` inherits no additional privileges from other roles.

### User-Defined Role Inherits from Other Roles

The following is a sample document for a user-defined role `appAdmin` defined for the `myApp` database: The document shows that the `appAdmin` role specifies privileges as well as inherits privileges from other roles:

```javascript
{
  _id: "myApp.appAdmin",
  role: "appAdmin",
  db: "myApp",
  privileges: [
      {
         resource: { db: "myApp", collection: "" },
         actions: [ "insert", "dbStats", "collStats", "compact" ]
      }
  ],
  roles: [
      { role: "appUser", db: "myApp" }
  ]
}
```

The `privileges` array lists the privileges that the `appAdmin` role specifies. This role has a single privilege that permits its actions ( `"insert"`, `"dbStats"`, `"collStats"`, `"compact"`) on all the collections in the `myApp` database excluding its system collections. See `resource-specific-db`.

The `roles` array lists the roles, identified by the role names and databases, from which the role `appAdmin` inherits privileges.
