---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/md5-and-scram-sha-1.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
