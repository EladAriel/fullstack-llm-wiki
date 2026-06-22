---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/query-password.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Type: string or array

Available in MongoDB Enterprise only.

The password used to bind to an LDAP server when using :setting:`~security.ldap.bind.queryUser`. You must use :setting:`~security.ldap.bind.queryPassword` with :setting:`~security.ldap.bind.queryUser`.

If not set, :binary:`~bin.mongod` or :binary:`~bin.mongos` does not attempt to bind to the LDAP server.

You can configure this setting on a running :binary:`~bin.mongod` or :binary:`~bin.mongos` using :dbcommand:`setParameter`.

The `ldapQueryPassword` :dbcommand:`setParameter` command accepts either a string or an array of strings. If `ldapQueryPassword` is set to an array, MongoDB tries each password in order until one succeeds. Use a password array to roll over the LDAP account password without downtime.

> **Note:**  Windows MongoDB deployments can use :setting:`~security.ldap.bind.useOSDefaults`
 instead of :setting:`~security.ldap.bind.queryUser` and
 :setting:`~security.ldap.bind.queryPassword`. You cannot specify both
 :setting:`~security.ldap.bind.queryPassword` and
 :setting:`~security.ldap.bind.useOSDefaults` at the same time.

Available in MongoDB Enterprise only.

The password used to bind to an LDAP server when using :option:`--ldapQueryUser`. You must use :option:`--ldapQueryPassword` with :option:`--ldapQueryUser`.

If not set, :program:`mongod` does not attempt to bind to the LDAP server.

You can configure this setting on a running :program:`mongod` using :dbcommand:`setParameter`.

The `ldapQueryPassword` :dbcommand:`setParameter` command accepts either a string or an array of strings. If `ldapQueryPassword` is set to an array, MongoDB tries each password in order until one succeeds. Use a password array to roll over the LDAP account password without downtime.

> **Note:**  Windows MongoDB deployments can use :option:`--ldapBindWithOSDefaults`
 instead of :option:`--ldapQueryUser` and :option:`--ldapQueryPassword`.
 You cannot specify both :option:`--ldapQueryPassword` and
 :option:`--ldapBindWithOSDefaults` at the same time.

Available in MongoDB Enterprise only.

The password used to bind to an LDAP server when using :option:`--ldapQueryUser`. You must use :option:`--ldapQueryPassword` with :option:`--ldapQueryUser`.

If not set, :program:`mongoldap` does not attempt to bind to the LDAP server.

You can configure this setting on a running :program:`mongoldap` using :dbcommand:`setParameter`.

The `ldapQueryPassword`:dbcommand:`setParameter` command accepts either a string or an array of strings. If `ldapQueryPassword` is set to an array, MongoDB tries each password in order until one succeeds. Use a password array to roll over the LDAP account password without downtime.

> **Note:**  Windows MongoDB deployments can use :option:`--ldapBindWithOSDefaults`
 instead of :option:`--ldapQueryUser` and :option:`--ldapQueryPassword`.
 You cannot specify both :option:`--ldapQueryPassword` and
 :option:`--ldapBindWithOSDefaults` at the same time.
