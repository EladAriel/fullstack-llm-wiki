---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getRoles.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# db.getRoles() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/access-roles-info.rst

## Examples

The examples in this section show how to use `db.getRoles` to:

- `db-getRoles-example-return-built-in-roles`
- `db-getRoles-example-auth-restrictions`
### Show Role Privileges and Built-In Roles

The following operation returns all the roles on the `products` database, including role privileges and built-in roles:

```javascript
use products

db.getRoles(
    {
      rolesInfo: 1,
      showPrivileges: true,
      showBuiltinRoles: true
    }
)
```

Example output (shortened for readability):

```javascript
{
  roles: [
    {
      role: 'dbOwner',
      db: 'products',
      isBuiltin: true,
      roles: [],
      inheritedRoles: [],
      privileges: [
        {
          resource: { db: 'products', collection: '' },
          actions: [
            'analyze',
            'bypassDocumentValidation',
            'changeCustomData',
            ...
          ]
        },
        {
          resource: { db: 'products', collection: 'system.profile' },
          actions: [
            'changeStream',
            'collStats',
            'convertToCapped',
            ...
          ]
        }
      ],
      inheritedPrivileges: [
        {
          resource: { db: 'products', collection: '' },
          actions: [
            'analyze',
            'bypassDocumentValidation',
            'changeCustomData',
            ...
          ]
        }
      ]
    },
    ...
  ]
}
```

### Show Authentication Restrictions

The following operation returns role inheritance information and authentication restrictions for all `user-defined roles <user-defined-roles>` on the `product` database:

```javascript
use products

db.getRoles( { rolesInfo: 1, showAuthenticationRestrictions: true } )
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
