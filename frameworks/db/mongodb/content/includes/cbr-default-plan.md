---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/cbr-default-plan.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.3, multi-planning with a CBR backup is the default plan selection mechanism for eligible queries. For a short trial period, the multi-planner attempts to find a plan capable of returning a result set within this short timeframe. If the attempt is unsuccessful, MongoDB applies a set of rules to determine whether the multi-planner should continue or if CBR should evaluate each node in the plan to determine the optimal plan.
