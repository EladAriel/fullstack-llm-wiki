---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/footnote-two-primaries-edge-cases.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In `some circumstances <edge-cases>`, two nodes in a replica set may transiently believe that they are the primary, but at most, one of them will be able to complete writes with :writeconcern:`{ w: "majority" } <"majority">` write concern. The node that can complete :writeconcern:`{ w: "majority" } <"majority">` writes is the current primary, and the other node is a former primary that has not yet recognized its demotion, typically due to a `network partition`. When this occurs, clients that connect to the former primary may observe stale data despite having requested read preference :readmode:`primary`, and new writes to the former primary will eventually roll back.
