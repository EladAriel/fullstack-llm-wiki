---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rs-8-enabled-modules.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.104746Z"
---
# Rs 8 Enabled Modules

| Database type | Automatically enabled capabilities |
|---------------|------------------------------------|
| RAM-only | [Redis Search]({{<relref "/operate/oss_and_stack/stack-with-enterprise/search">}})<br />[JSON]({{<relref "/operate/oss_and_stack/stack-with-enterprise/json">}})<br />[Time series]({{<relref "/operate/oss_and_stack/stack-with-enterprise/timeseries">}})<br />[Probabilistic]({{<relref "/operate/oss_and_stack/stack-with-enterprise/bloom">}})  |
| Flash-enabled ([Redis Flex]({{<relref "/operate/rs/databases/flash">}})) | [JSON]({{<relref "/operate/oss_and_stack/stack-with-enterprise/json">}})<br />[Probabilistic]({{<relref "/operate/oss_and_stack/stack-with-enterprise/bloom">}}) |
| [Active-Active]({{<relref "/operate/rs/databases/active-active">}})<sup>[1](#enabled-modules-table-note-1)</sup> | [Redis Search]({{<relref "/operate/oss_and_stack/stack-with-enterprise/search/search-active-active">}})<br />[JSON]({{<relref "/operate/oss_and_stack/stack-with-enterprise/json">}}) |

1. <a name="enabled-modules-table-note-1"></a>Upgrading existing Active-Active databases to Redis version 8 does not automatically enable these capabilities. Only new Active-Active databases created with Redis version 8 enable these capabilities by default.