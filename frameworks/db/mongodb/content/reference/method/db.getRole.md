---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# db.getRole() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/access-roles-info.rst

## Examples

The examples in this section show how to use `db.getRoles` to:

- `db-getRole-example-inheritance`
- `db-getRole-example-privileges`
- `db-getRole-example-auth-restrictions`
### Show Role Inheritance Information

The following operation returns role inheritance information for the role `associate` defined on the `products` database:

```javascript
use products
db.getRole( "associate" )
```

Example output:

```javascript
{
  _id: 'products.associate',
  role: 'associate',
  db: 'products',
  roles: [ { role: 'readWrite', db: 'products' } ],
  inheritedRoles: [ { role: 'readWrite', db: 'products' } ],
  isBuiltin: false
}
```

### Show Role Privileges

The following operation returns role inheritance information and privileges for the role `associate` defined on the `products` database:

```javascript
use products
db.getRole( "associate", { showPrivileges: true } )
```

Example output:

```javascript
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
        'convertToCapped',
        'createCollection',
        'createIndex',
        'dbHash',
        'dbStats',
        'dropCollection',
        'dropIndex',
        'find',
        'insert',
        'killCursors',
        'listCollections',
        'listIndexes',
        'planCacheRead',
        'remove',
        'renameCollectionSameDB',
        'update'
      ]
    }
  ],
  isBuiltin: false
}
```

### Show Authentication Restrictions

The following operation returns role inheritance information and authentication restrictions for the role `associate` defined on the `products` database:

```javascript
use products
db.getRole( "associate", { showAuthenticationRestrictions: true } )
```

Example output:

```javascript
{
  _id: 'products.associate',
  role: 'associate',
  db: 'products',
  roles: [ { role: 'readWrite', db: 'products' } ],
  authenticationRestrictions: [
    [ { clientSource: [ '198.51.100.0' ] } ]
  ],
  inheritedRoles: [ { role: 'readWrite', db: 'products' } ],
  inheritedAuthenticationRestrictions: [
    [ { clientSource: [ '198.51.100.0' ] } ]
  ],
  isBuiltin: false
}
```
