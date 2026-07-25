---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/cbr-default-plan.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.3, multi-planning with a CBR backup is the default plan selection mechanism for eligible queries. For a short trial period, the multi-planner attempts to find a plan capable of returning a result set within this short timeframe. If the attempt is unsuccessful, MongoDB applies a set of rules to determine whether the multi-planner should continue or if CBR should evaluate each node in the plan to determine the optimal plan.
