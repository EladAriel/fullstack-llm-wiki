---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rdi-vm-reqs.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.093621Z"
---
# Rdi Vm Reqs

* **CPU**: A minimum of 4 CPU cores. You should consider adding
  2-6 extra cores on top of this if your dataset is big and you want to ingest the
  baseline snapshot as fast as possible.
* **RAM**: 8GB 
* **Disk**: On top of the OS footprint,
  RDI requires 20GB in the `/var` folder and 1GB in the `/opt` folder (to
  store the log files). This allows space for upgrades.
* **Network interface**: 10GB or more.