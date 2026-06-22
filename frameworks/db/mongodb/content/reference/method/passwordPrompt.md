---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/passwordPrompt.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# passwordPrompt() (mongosh method)

## Definition

## Examples

### Use `passwordPrompt()` with `db.createUser()`

The :method:`db.createUser()` requires a password to be specified.

You can use :method:`passwordPrompt()` as the value for the `pwd` instead of specifying the password.

```javascript
db.createUser( { 
   user:"user123",
   pwd: passwordPrompt(),   // Instead of specifying the password in cleartext
   roles:[ "readWrite" ]
} )
```

Enter the password when prompted.

### Use `passwordPrompt()` with `db.auth()`

When you run the `db-auth-syntax-username-password` command you can replace the password with the :method:`passwordPrompt()` method.

If you omit the password from the `db-auth-syntax-username-password` command, the user is prompted to enter a password.

The following example prompts the user to enter a password which is not displayed in the shell:

```javascript
db.auth("user123")
```

### Use `passwordPrompt()` with `db.changeUserPassword()`

The :method:`db.changeUserPassword()` requires a password to be specified.

You can use :method:`passwordPrompt()` instead of specifying the password.

```javascript
db.changeUserPassword("user123", passwordPrompt())
```

Enter the password when prompted.

### Use `passwordPrompt()` with `db.updateUser()`

When changing the password with :method:`db.updateUser()`, the method requires a password to be specified.

You can use :method:`passwordPrompt()` as the value for the `pwd` instead of specifying the password.

```javascript
db.updateUser(
   "user123",
   {
     pwd: passwordPrompt(),
     mechanisms: [ "SCRAM-SHA-256" ]
   }
)
```

Enter the password when prompted.
