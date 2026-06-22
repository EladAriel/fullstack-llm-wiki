---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tlsFIPSMode_SCRAM-SHA-1.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.3, you cannot specify `SCRAM-SHA-1` for :parameter:`authenticationMechanisms` while also specifying :option:`mongod --tlsFIPSMode` or :option:`mongos --tlsFIPSMode`.

If you try to specify `SCRAM-SHA-1` for `authenticationMechanisms` while also specifying `--tlsFIPSMode`, the server throws an error and logs a message similar to the following:

```none
SCRAM-SHA-1 is not allowed in FIPS mode.
```
