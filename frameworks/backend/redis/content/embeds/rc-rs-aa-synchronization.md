---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-rs-aa-synchronization.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
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