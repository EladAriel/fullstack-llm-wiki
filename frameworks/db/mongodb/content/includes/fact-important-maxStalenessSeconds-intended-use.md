---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-important-maxStalenessSeconds-intended-use.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** The `maxStalenessSeconds` read preference option is intended for
applications that read from secondaries and want to avoid reading
from a secondary that has fallen overly far behind in replicating
the primary's writes. For example, a secondary might stop
replicating due to a network outage between itself and the primary.
In that case, the client should stop reading from the secondary
until an administrator resolves the outage and the secondary catches
up.
