---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-split-horizon-binding.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To configure cluster nodes for [split horizon DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS)_, use host names instead of IP addresses.

Starting in MongoDB v5.0, :dbcommand:`replSetInitiate` and :dbcommand:`replSetReconfig` reject configurations that use IP addresses instead of hostnames.

Use :parameter:`disableSplitHorizonIPCheck` to modify nodes that cannot be updated to use host names. The parameter only applies to the configuration commands.

:binary:`mongod` and :binary:`mongos` do not rely on :parameter:`disableSplitHorizonIPCheck` for validation at startup. Legacy :binary:`mongod` and :binary:`mongos` instances that use IP addresses instead of host names can start after an upgrade.

Instances that are configured with IP addresses log a warning to use host names instead of IP addresses.
