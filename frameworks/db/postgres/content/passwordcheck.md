---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/passwordcheck.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## passwordcheck -- verify password strength

passwordcheck

The `passwordcheck` module checks users' passwords whenever they are set with `sql-createrole` or `sql-alterrole`. If a password is considered too weak, it will be rejected and the command will terminate with an error.

To enable this module, add `'$libdir/passwordcheck'` to `guc-shared-preload-libraries` in `postgresql.conf`, then restart the server.

You can adapt this module to your needs by changing the source code. For example, you can use [CrackLib](https://github.com/cracklib/cracklib) to check passwords -- this only requires uncommenting two lines in the `Makefile` and rebuilding the module. (We cannot include CrackLib by default for license reasons.) Without CrackLib, the module enforces a few simple rules for password strength, which you can modify or extend as you see fit.

To prevent unencrypted passwords from being sent across the network, written to the server log or otherwise stolen by a database administrator, PostgreSQL allows the user to supply pre-encrypted passwords. Many client programs make use of this functionality and encrypt the password before sending it to the server. This limits the usefulness of the `passwordcheck` module, because in that case it can only try to guess the password. For this reason, `passwordcheck` is not recommended if your security requirements are high. It is more secure to use an external authentication method such as GSSAPI (see `client-authentication`) than to rely on passwords within the database. Alternatively, you could modify `passwordcheck` to reject pre-encrypted passwords, but forcing users to set their passwords in clear text carries its own security risks.

## Configuration Parameters

- The minimum acceptable password length in bytes. The default is 8. Only superusers can change this setting. This parameter has no effect if a user supplies a pre-encrypted password.

In ordinary usage, this parameter is set in `postgresql.conf`, but superusers can alter it on-the-fly within their own sessions. Typical usage might be:

```
# postgresql.conf
passwordcheck.min_password_length = 12
```
