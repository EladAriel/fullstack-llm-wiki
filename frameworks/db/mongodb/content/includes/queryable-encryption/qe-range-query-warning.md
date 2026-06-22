---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-range-query-warning.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** {+qe+} defends against data exfiltration, not against adversaries with
persistent access to an environment, or those who can retrieve both
database snapshots and accompanying query transcripts/logs.

When using {+qe+}, equality and range queries offer similar security against attackers with database snapshots. However, an attacker with access to both database snapshots and query information is beyond the scope of {+qe+}'s security guarantees. This is **especially** true for range queries, even if only a small number of query transcripts or logs are retrieved. See [6.1: Range Queries in the Persistent Model](https://cdn.bfldr.com/2URK6TO/as/64kp46t53v34xw37gkngbrg/An_Overview_of_Queryable_Encryption)_ in the overview whitepaper for details.
