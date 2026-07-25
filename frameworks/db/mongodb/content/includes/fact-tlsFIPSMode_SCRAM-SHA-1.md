---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tlsFIPSMode_SCRAM-SHA-1.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.3, you cannot specify `SCRAM-SHA-1` for :parameter:`authenticationMechanisms` while also specifying :option:`mongod --tlsFIPSMode` or :option:`mongos --tlsFIPSMode`.

If you try to specify `SCRAM-SHA-1` for `authenticationMechanisms` while also specifying `--tlsFIPSMode`, the server throws an error and logs a message similar to the following:

```none
SCRAM-SHA-1 is not allowed in FIPS mode.
```
