---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-no-ip-addresses-in-split-horizons.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** Starting in MongDB 5.0, `split horizon DNS
<https://en.wikipedia.org/wiki/Split-horizon_DNS>`__ nodes that are
only configured with an IP address fail startup validation and
report an error. See :parameter:`disableSplitHorizonIPCheck`.
