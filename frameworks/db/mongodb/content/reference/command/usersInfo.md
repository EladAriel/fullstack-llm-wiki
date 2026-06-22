---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/usersInfo.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# usersInfo (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     usersInfo: <various>,
     showCredentials: <Boolean>,
     showCustomData: <Boolean>,
     showPrivileges: <Boolean>,
     showAuthenticationRestrictions: <Boolean>,
     filter: <document>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

## `usersInfo: <various>`

```javascript
{ usersInfo: <various> }
```

The argument to `usersInfo` has multiple forms depending on the requested information:

## Required Access

Users can always view their own information.

To view another user's information, the user running the command must have privileges that include the :authaction:`viewUser` action on the other user's database.

## Output

The following information can be returned by the :dbcommand:`usersInfo` depending on the options specified:

```javascript
{
   "users" : [
      {
         "_id" : "<db>.<username>",
         "userId" : <UUID>,
         "user" : "<username>",
         "db" : "<db>",
         "mechanisms" : [ ... ],
         "customData" : <document>,
         "roles" : [ ... ],
         "credentials": { ... }, // only if showCredentials: true
         "inheritedRoles" : [ ... ],  // only if showPrivileges: true or showAuthenticationRestrictions: true
         "inheritedPrivileges" : [ ... ], // only if showPrivileges: true or showAuthenticationRestrictions: true
         "inheritedAuthenticationRestrictions" : [ ] // only if showPrivileges: true or showAuthenticationRestrictions: true
         "authenticationRestrictions" : [ ... ] // only if showAuthenticationRestrictions: true
      },
      ...
   ],
   "ok" : 1
}
```

## Examples

### View Specific Users

To see information and privileges, but not the credentials, for the user `"Kari"` defined in `"home"` database, run the following command:

```javascript
db.runCommand(
   {
     usersInfo:  { user: "Kari", db: "home" },
     showPrivileges: true
   }
)
```

To view a user that exists in the current database, you can specify the user by name only. For example, if you are in the `home` database and a user named `"Kari"` exists in the `home` database, you can run the following command:

```javascript
db.getSiblingDB("home").runCommand(
   {
     usersInfo:  "Kari",
     showPrivileges: true
   }
)
```

### View Multiple Users

To view info for several users, use an array, with or without the optional fields `showPrivileges` and `showCredentials`. For example:

```javascript
db.runCommand( {
   usersInfo: [ { user: "Kari", db: "home" }, { user: "Li", db: "myApp" } ],
   showPrivileges: true
} )
```

### View All Users for a Database

To view all users on the database the command is run, use a command document that resembles the following:

```javascript
db.runCommand( { usersInfo: 1 } )
```

When viewing all users, you can specify the `showCredentials` option but not the `showPrivileges` or the `showAuthenticationRestrictions` options.

### View All Users for a Database that Match the Specified Filter

The :dbcommand:`usersInfo` command can accept a `filter` document to return information for users that match the filter condition.

To view all users in the current database who have the specified role, use a command document that resembles the following:

```javascript
db.runCommand( { usersInfo: 1, filter: { roles: { role: "root", db: "admin" } } } )
```

When viewing all users, you can specify the `showCredentials` option but not the `showPrivileges` or the `showAuthenticationRestrictions` options.

### View All Users with `SCRAM-SHA-1` Credentials

The :dbcommand:`usersInfo` command can accept a `filter` document to return information for users that match the filter condition.

The following operation returns all users that have `SCRAM-SHA-1` credentials. Specifically, the command returns all users across all databases and then uses the :pipeline:`$match` stage to apply the specified filter to the users.

```javascript
db.runCommand( { usersInfo: { forAllDBs: true}, filter: { mechanisms: "SCRAM-SHA-1" } } )
```

When viewing all users, you can specify the `showCredentials` option but not the `showPrivileges` or the `showAuthenticationRestrictions` options.

### Omit Custom Data from Output

.. versionadded:: 5.2

.. include:: /includes/fact-omit-custom-data-example-setup.rst

To retrieve the user but omit the custom data from the output, run :dbcommand:`usersInfo` with `showCustomData` set to `false`:

```javascript
db.getSiblingDB("products").runCommand ( {
   usersInfo: "accountAdmin01",
   showCustomData: false 
} )
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
