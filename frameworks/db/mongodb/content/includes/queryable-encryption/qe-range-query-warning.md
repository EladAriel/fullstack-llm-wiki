---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-range-query-warning.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** {+qe+} defends against data exfiltration, not against adversaries with
persistent access to an environment, or those who can retrieve both
database snapshots and accompanying query transcripts/logs.

When using {+qe+}, equality and range queries offer similar security against attackers with database snapshots. However, an attacker with access to both database snapshots and query information is beyond the scope of {+qe+}'s security guarantees. This is **especially** true for range queries, even if only a small number of query transcripts or logs are retrieved. See [6.1: Range Queries in the Persistent Model](https://cdn.bfldr.com/2URK6TO/as/64kp46t53v34xw37gkngbrg/An_Overview_of_Queryable_Encryption)_ in the overview whitepaper for details.
