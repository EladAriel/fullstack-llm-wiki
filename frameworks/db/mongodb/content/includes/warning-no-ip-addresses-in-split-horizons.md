---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-no-ip-addresses-in-split-horizons.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** Starting in MongDB 5.0, `split horizon DNS
<https://en.wikipedia.org/wiki/Split-horizon_DNS>`__ nodes that are
only configured with an IP address fail startup validation and
report an error. See :parameter:`disableSplitHorizonIPCheck`.
