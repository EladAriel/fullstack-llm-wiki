---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.auth.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# db.auth() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`db.auth()` has the following syntax forms:

### `db.auth(<username>, <password>)`

You can either:

- Omit the password to prompt the user to enter a password:
```javascript
   db.auth( <username> )
```

- Use :method:`passwordPrompt()` to prompt the user to enter
a password:

```javascript
   db.auth( <username>, passwordPrompt() )
```

- Specify a cleartext password.
```javascript
   db.auth( <username>, <password> )
```

### `db.auth(<user document>)`

```javascript
db.auth( {
   user: <username>,
   pwd: passwordPrompt(),   // Or "<cleartext password>"
   mechanism: <authentication mechanism>,
   digestPassword: <boolean>
} )
```

.. include:: /includes/note-auth-methods-excluded-from-shell-history.rst

Returns :method:`db.auth()` returns `0` when authentication is **not** successful, and `1` when the operation is successful.

## Behavior

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

## Example

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst
.. include:: /includes/extracts/4.4-changes-passwordPrompt.rst

### Authenticate after Connecting to the Shell

To authenticate after connecting :binary:`~bin.mongosh`, issue :method:`db.auth()` in the user's `authentication database <authentication-database>`:

```javascript
use test
db.auth( "myTestDBUser", passwordPrompt() )
```

You can omit the `password` value entirely to prompt the user to enter their password:

```javascript
use test
db.auth( "myTestDBUser" )
```

Starting in MongoDB 5.0, if your connection specifies the `--apiStrict` option, you may not use the :method:`db.auth()` method to:

- Authenticate again as the same user on the same database.
- Authenticate as a different user when previously authenticated
on the same database.

- Authenticate with a new database when previously authenticated on a
different database.

### Authenticate when Connecting to the Shell

Alternatively, you can use :binary:`~bin.mongosh`'s command-line options :option:`--username <mongosh --username>`, :option:`--password <mongosh --password>`, :option:`--authenticationDatabase <mongosh --authenticationDatabase>`, and :option:`--authenticationMechanism <mongosh --authenticationMechanism>` to specify authentication credentials when connecting :binary:`~bin.mongosh`:

```bash
mongosh --username "myTestDBUser" --password --authenticationDatabase test --authenticationMechanism SCRAM-SHA-256
```
