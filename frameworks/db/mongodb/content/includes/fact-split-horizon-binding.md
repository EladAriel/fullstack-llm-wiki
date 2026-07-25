---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-split-horizon-binding.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To configure cluster nodes for split horizon DNS, use host names instead of IP addresses.

Starting in MongoDB v5.0, :dbcommand:`replSetInitiate` and :dbcommand:`replSetReconfig` reject configurations that use IP addresses instead of hostnames.

Use :parameter:`disableSplitHorizonIPCheck` to modify nodes that cannot be updated to use host names. The parameter only applies to the configuration commands.

:binary:`mongod` and :binary:`mongos` do not rely on `disableSplitHorizonIPCheck` for validation at startup. Legacy `mongod` and `mongos` instances that use IP addresses instead of host names can start after an upgrade.

Instances that are configured with IP addresses log a warning to use host names instead of IP addresses.
