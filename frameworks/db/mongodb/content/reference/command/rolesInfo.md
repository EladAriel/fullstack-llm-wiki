---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/rolesInfo.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# rolesInfo (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {  
     rolesInfo: { role: <name>, db: <db> },
     showAuthenticationRestrictions: <Boolean>,
     showBuiltinRoles: <Boolean>,
     showPrivileges: <Boolean>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

## Behavior

### Return Information for a Single Role

To specify a role from the current database, specify the role by its name:

```javascript
{ rolesInfo: "<rolename>" }
```

To specify a role from another database, specify the role by a document that specifies the role and database:

```javascript
{ rolesInfo: { role: "<rolename>", db: "<database>" } }
```

### Return Information for Multiple Roles

To specify multiple roles, use an array. Specify each role in the array as a document or string. Use a string only if the role exists on the database on which the command runs:

```javascript
{
  rolesInfo: [
     "<rolename>",
     { role: "<rolename>", db: "<database>" },
     ...
  ]
}
```

### Return Information for All Roles in the Database

To specify all roles in the database on which the command runs, specify `rolesInfo: 1`. By default MongoDB displays all the `user-defined roles <user-defined-roles>` in the database. To include `built-in roles <built-in-roles>` as well, include the parameter-value pair `showBuiltinRoles: true`:

```javascript
{ rolesInfo: 1, showBuiltinRoles: true }
```

## Required Access

.. include:: /includes/access-roles-info.rst

## Output

## Examples

The examples in this section show how to use the `rolesInfo` command to:

- `rolesInfo-example-single-role`
- `rolesInfo-example-multiple-roles`
- `rolesInfo-example-user-defined-roles`
- `rolesInfo-example-user-defined-and-built-in-roles`
- `rolesInfo-example-auth-restrictions`
### View Information for a Single Role

The following command returns the role inheritance information for the role `associate` defined in the `products` database:

```javascript
db.runCommand(
    {
      rolesInfo: { role: "associate", db: "products" }
    }
)
```

The following command returns the role inheritance information for the role `siteManager` on the database on which the command runs:

```javascript
db.runCommand(
    {
      rolesInfo: "siteManager"
    }
)
```

The following command returns both the role inheritance and the privileges for the role `associate` defined on the `products` database:

```javascript
db.runCommand(
    {
      rolesInfo: { role: "associate", db: "products" },
      showPrivileges: true
    }
)
```

### View Information for Multiple Roles

The following command returns information for two roles on two different databases:

```javascript
db.runCommand(
    {
      rolesInfo: [
         { role: "associate", db: "products" },
         { role: "manager", db: "resources" }
      ]
    }
)
```

The following returns both the role inheritance and the privileges:

```javascript
db.runCommand(
    {
      rolesInfo: [
         { role: "associate", db: "products" },
         { role: "manager", db: "resources" }
      ],
      showPrivileges: true
    }
)
```

### View All User-Defined Roles for a Database

The following operation returns all `user-defined roles <user-defined-roles>` on the database on which the command runs and includes privileges:

```javascript
db.runCommand(
    {
      rolesInfo: 1,
      showPrivileges: true
    }
)
```

Example output (shortened for readability):

```javascript
{
  roles: [
    {
      _id: 'products.associate',
      role: 'associate',
      db: 'products',
      privileges: [
        {
          resource: { db: 'products', collection: '' },
          actions: [ 'bypassDocumentValidation' ]
        }
      ],
      roles: [ { role: 'readWrite', db: 'products' } ],
      isBuiltin: false,
      inheritedRoles: [ { role: 'readWrite', db: 'products' } ],
      inheritedPrivileges: [
        {
          resource: { db: 'products', collection: '' },
          actions: [ 'bypassDocumentValidation' ]
        },
        {
          resource: { db: 'products', collection: '' },
          actions: [
            'changeStream',
            'collStats',
            'compactStructuredEncryptionData',
            ...
          ]
        },
        ...
      ]
    }
  ],
  ok: 1
}
```

### View All User-Defined and Built-In Roles for a Database

The following operation returns all roles on the database on which the command runs, including both built-in and user-defined roles:

```javascript
db.runCommand(
    {
      rolesInfo: 1,
      showBuiltinRoles: true
    }
)
```

Example output (shortened for readability):

```javascript
{
  roles: [
    {
      role: 'enableSharding',
      db: 'products',
      isBuiltin: true,
      roles: [],
      inheritedRoles: []
    },
    {
      role: 'userAdmin',
      db: 'products',
      isBuiltin: true,
      roles: [],
      inheritedRoles: []
    },
    {
      role: 'read',
      db: 'products',
      isBuiltin: true,
      roles: [],
      inheritedRoles: []
    },
    ...
  ],
  ok: 1
}
```

### View Authentication Restrictions for Roles

The following operation returns all user-defined roles on the `products` database and includes authentication restrictions:

```javascript
db.runCommand(
    {
      rolesInfo: 1,
      showAuthenticationRestrictions: true
    }
)
```

Example output:

```javascript
{
  roles: [
    {
      _id: 'products.associate',
      role: 'associate',
      db: 'products',
      roles: [ { role: 'readWrite', db: 'products' } ],
      authenticationRestrictions: [
        [ { clientSource: [ '198.51.100.0' ] } ]
      ],
      isBuiltin: false,
      inheritedRoles: [ { role: 'readWrite', db: 'products' } ],
      inheritedAuthenticationRestrictions: [
        [ { clientSource: [ '198.51.100.0' ] } ]
      ]
    }
  ],
  ok: 1
}
```
