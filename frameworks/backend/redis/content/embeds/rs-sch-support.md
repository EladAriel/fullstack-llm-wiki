---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rs-sch-support.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

| Upgrade method | SCH support | Expected behavior |
| --- | --- | --- |
| [Rolling upgrade]({{< relref "/operate/rs/installing-upgrading/upgrading/upgrade-cluster#rolling-upgrade" >}}) | Full | New nodes and old ones removed sequentially. SCH pre-handoffs and relaxed timeouts greatly reduce disruptions during the upgrade. |
| [In-place upgrade]({{< relref "/operate/rs/installing-upgrading/upgrading/upgrade-cluster#in-place-upgrade" >}}) | Partial | Relaxed timeouts reduce errors but there are no pre-handoffs. Disconnections occur when processes are replaced during the upgrade, so clients should rely on auto-reconnect, which will cause brief lapses in service. |
| [Maintenance mode]({{< relref "/operate/rs/clusters/maintenance-mode" >}}) | Full | SCH is fully supported during hardware or OS patching operations. Pre-handoffs and relaxed timeouts minimize application impact. |
