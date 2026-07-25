---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-3.4-built-in-roles-changes.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The privileges of the following built-in roles no longer apply to the `local` and `config` databases:

Correspondingly, the following built-in roles include additional read and write privileges on `local` and `config` databases:

- :authrole:`clusterManager`
- :authrole:`clusterMonitor`
- :authrole:`backup`
- :authrole:`restore`.
