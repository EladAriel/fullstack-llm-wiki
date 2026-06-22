---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-ocsp-enabled.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 6.0, if :parameter:`ocspEnabled` is set to `true` during initial sync, all nodes must be able to reach the `OCSP <ocsp-support>` responder.

If a member fails in the :replstate:`STARTUP2` state, set :parameter:`tlsOCSPVerifyTimeoutSecs` to a value that is less than `5`.
