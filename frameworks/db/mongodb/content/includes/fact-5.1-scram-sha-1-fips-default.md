---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.1-scram-sha-1-fips-default.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.1, instances running in `FIPS mode <fips-overview>` have the `SCRAM-SHA-1 authentication mechanism <authentication-parameters>` disabled by default. You can enable the `SCRAM-SHA-1 authentication mechanism <authentication-parameters>` with the `setParameter.authenticationMechanisms <set-parameter-authenticationMechanisms-code>` command.

This change will not affect drivers which target MongoDB :dbcommand:`setFeatureCompatibilityVersion` 4.0+.
