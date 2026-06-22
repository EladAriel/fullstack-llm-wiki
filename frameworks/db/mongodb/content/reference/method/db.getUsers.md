---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getUsers.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# db.getUsers() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/access-user-info.rst

## Examples

### View All Users for a Database that Match the Specified Filter

The :method:`db.getUsers()` method can accept a `filter` document to return information for users that match the filter condition.

To view all users for the current database who have `SCRAM-SHA-256` credentials:

```javascript
db.getUsers({ filter: { mechanisms: "SCRAM-SHA-256" } })
```

When viewing all users, you can specify the `showCredentials` option but not the `showPrivileges` or the `showAuthenticationRestrictions` options.

### Omit Custom Data from Output

.. versionadded:: 5.2

.. include:: /includes/fact-omit-custom-data-example-setup.rst

To retrieve the user but omit the custom data from the output, run :method:`db.getUsers()` with `showCustomData` set to `false`:

```javascript
db.getSiblingDB("products").getUsers( { showCustomData: false } )
```

Example output:

```javascript
{
   users: [
     {
       _id: 'products.accountAdmin01',
       userId: UUID("0955afc1-303c-4683-a029-8e17dd5501f4"),
       user: 'accountAdmin01',
       db: 'products',
       roles: [ { role: 'readWrite', db: 'products' } ],
       mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ]
     }
   ],
   ok: 1
}
```
