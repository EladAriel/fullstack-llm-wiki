---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/waitForDelete-warning.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When the `_waitForDelete` field is set to `true`, MongoDB does not wait on the :parameter:`orphanCleanupDelaySecs delay before performing the range deletion. If you use the waitForDelete` parameter and have any read operations occurring on secondaries, the read might terminate due to the migration's delete phase. To learn more, see :parameter:`terminateSecondaryReadsOnOrphanCleanup`.
