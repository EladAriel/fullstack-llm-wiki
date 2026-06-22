---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-rs-aa-synchronization.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

In the example below, database writes are concurrent at the points in
time t1 and t2 and happen before a sync can communicate the changes.
However, writes at times t4 and t6 are not concurrent as a sync happened
in between.

|  **Time** | **CRDB Instance1** | **CRDB Instance2** |
|  ------: | :------: | :------: |
|  t1 | SET key1 "a" |  |
|  t2 |  | SET key1 "b" |
|  t3 | — Sync — | — Sync — |
|  t4 | SET key1 "c" |  |
|  t5 | — Sync — | — Sync — |
|  t6 |  | SET key1 "d" |