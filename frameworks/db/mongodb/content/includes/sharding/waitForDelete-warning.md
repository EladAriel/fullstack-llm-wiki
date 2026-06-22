---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/waitForDelete-warning.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When the `_waitForDelete` field is set to `true`, MongoDB does not wait on the :parameter:`orphanCleanupDelaySecs delay before performing the range deletion. If you use the waitForDelete` parameter and have any read operations occurring on secondaries, the read might terminate due to the migration's delete phase. To learn more, see :parameter:`terminateSecondaryReadsOnOrphanCleanup`.
