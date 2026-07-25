---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getUser.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# db.getUser() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/access-user-info.rst

## Examples

The following operations return information about an example `appClient` user in an `accounts` database:

```javascript
use accounts
db.getUser("appClient")
```

Example output:

```javascript
{
   _id: 'accounts.appClient',
   userId: UUID("1c2fc1bf-c4dc-4a22-8b04-3971349ce0dc"),
   user: 'appClient',
   db: 'accounts',
   roles: [],
   mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ]
}
```

### Omit Custom Data from Output

.. versionadded:: 5.2

.. include:: /includes/fact-omit-custom-data-example-setup.rst

To retrieve the user but omit the custom data from the output, run :method:`db.getUser()` with `showCustomData` set to `false`:

```javascript
db.getSiblingDB("products").getUser(
   "accountAdmin01",
   { showCustomData: false }
)
```

Example output:

```javascript
{
   _id: 'products.accountAdmin01',
   userId: UUID("0955afc1-303c-4683-a029-8e17dd5501f4"),
   user: 'accountAdmin01',
   db: 'products',
   roles: [ { role: 'readWrite', db: 'products' } ],
   mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ]
}
```
