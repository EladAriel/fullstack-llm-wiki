---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/fact-parameters-cache-pressure.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In rare circumstances, a write can fail due to cache pressure. When this happens MongoDB issues a `TemporarilyUnavailable` error and increments the `temporarilyUnavailableErrors` counter in two places: the slow query log and the `Full Time Diagnostic Data Capture (FTDC) <ftdc-stub>`.

Individual operations within multi-document transactions never return `TemporarilyUnavailable` errors.

Adjust the write retry properties by modifying the :parameter:`temporarilyUnavailableBackoffBaseMs` and :parameter:`temporarilyUnavailableMaxRetries` parameters.
