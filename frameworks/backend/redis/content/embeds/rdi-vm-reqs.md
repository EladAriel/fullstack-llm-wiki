---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rdi-vm-reqs.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

* **CPU**: A minimum of 4 CPU cores. You should consider adding
  2-6 extra cores on top of this if your dataset is big and you want to ingest the
  baseline snapshot as fast as possible.
* **RAM**: 8GB 
* **Disk**: On top of the OS footprint,
  RDI requires 20GB in the `/var` folder and 1GB in the `/opt` folder (to
  store the log files). This allows space for upgrades.
* **Network interface**: 10GB or more.