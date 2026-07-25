---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/fact-parameters-cache-pressure.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In rare circumstances, a write can fail due to cache pressure. When this happens MongoDB issues a `TemporarilyUnavailable` error and increments the `temporarilyUnavailableErrors` counter in two places: the slow query log and the `Full Time Diagnostic Data Capture (FTDC) <ftdc-stub>`.

Individual operations within multi-document transactions never return `TemporarilyUnavailable` errors.

Adjust the write retry properties by modifying the :parameter:`temporarilyUnavailableBackoffBaseMs` and :parameter:`temporarilyUnavailableMaxRetries` parameters.
