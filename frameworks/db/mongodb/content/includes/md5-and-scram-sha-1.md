---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/md5-and-scram-sha-1.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If you use `SCRAM-SHA-1 <authentication-parameters>`:

- `md5` is necessary but is not used for cryptographic purposes,
and

- if you use `FIPS mode <fips-overview>`, then instead of
`SCRAM-SHA-1 <authentication-parameters>` use:

- `SCRAM-SHA-256 <authentication-scram>`,
- `Kerberos <security-kerberos>`,
- `LDAP <security-ldap>`, or
- `X.509 <security-auth-x509>`
