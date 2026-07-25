---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.1-scram-sha-1-fips-default.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.1, instances running in `FIPS mode <fips-overview>` have the `SCRAM-SHA-1 authentication mechanism <authentication-parameters>` disabled by default. You can enable the `SCRAM-SHA-1 authentication mechanism <authentication-parameters>` with the `setParameter.authenticationMechanisms <set-parameter-authenticationMechanisms-code>` command.

This change will not affect drivers which target MongoDB :dbcommand:`setFeatureCompatibilityVersion` 4.0+.
