---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/query-password.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Type: string or array

Available in MongoDB Enterprise only.

The password used to bind to an LDAP server when using :setting:`~security.ldap.bind.queryUser`. You must use :setting:`~security.ldap.bind.queryPassword` with `queryUser`.

If not set, :binary:`~bin.mongod` or :binary:`~bin.mongos` does not attempt to bind to the LDAP server.

You can configure this setting on a running `mongod` or `mongos` using :dbcommand:`setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a string or an array of strings. If `ldapQueryPassword` is set to an array, MongoDB tries each password in order until one succeeds. Use a password array to roll over the LDAP account password without downtime.

> **Note:**  Windows MongoDB deployments can use :setting:`~security.ldap.bind.useOSDefaults`
 instead of `queryUser` and
 `queryPassword`. You cannot specify both
 `queryPassword` and
 `useOSDefaults` at the same time.

Available in MongoDB Enterprise only.

The password used to bind to an LDAP server when using :option:`--ldapQueryUser`. You must use :option:`--ldapQueryPassword` with `--ldapQueryUser`.

If not set, :program:`mongod` does not attempt to bind to the LDAP server.

You can configure this setting on a running :program:`mongod` using `setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a string or an array of strings. If `ldapQueryPassword` is set to an array, MongoDB tries each password in order until one succeeds. Use a password array to roll over the LDAP account password without downtime.

> **Note:**  Windows MongoDB deployments can use :option:`--ldapBindWithOSDefaults`
 instead of `--ldapQueryUser` and `--ldapQueryPassword`.
 You cannot specify both `--ldapQueryPassword` and
 `--ldapBindWithOSDefaults` at the same time.

Available in MongoDB Enterprise only.

The password used to bind to an LDAP server when using `--ldapQueryUser`. You must use `--ldapQueryPassword` with `--ldapQueryUser`.

If not set, :program:`mongoldap` does not attempt to bind to the LDAP server.

You can configure this setting on a running :program:`mongoldap` using `setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a string or an array of strings. If `ldapQueryPassword` is set to an array, MongoDB tries each password in order until one succeeds. Use a password array to roll over the LDAP account password without downtime.

> **Note:**  Windows MongoDB deployments can use `--ldapBindWithOSDefaults`
 instead of `--ldapQueryUser` and `--ldapQueryPassword`.
 You cannot specify both `--ldapQueryPassword` and
 `--ldapBindWithOSDefaults` at the same time.
