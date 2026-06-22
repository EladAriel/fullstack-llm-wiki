---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rs-8-enabled-modules.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

| Database type | Automatically enabled capabilities |
|---------------|------------------------------------|
| RAM-only | [Search and query]({{<relref "/operate/oss_and_stack/stack-with-enterprise/search">}})<br />[JSON]({{<relref "/operate/oss_and_stack/stack-with-enterprise/json">}})<br />[Time series]({{<relref "/operate/oss_and_stack/stack-with-enterprise/timeseries">}})<br />[Probabilistic]({{<relref "/operate/oss_and_stack/stack-with-enterprise/bloom">}})  |
| Flash-enabled ([Redis Flex]({{<relref "/operate/rs/databases/flash">}})) | [JSON]({{<relref "/operate/oss_and_stack/stack-with-enterprise/json">}})<br />[Probabilistic]({{<relref "/operate/oss_and_stack/stack-with-enterprise/bloom">}}) |
| [Active-Active]({{<relref "/operate/rs/databases/active-active">}})<sup>[1](#enabled-modules-table-note-1)</sup> | [Search and query]({{<relref "/operate/oss_and_stack/stack-with-enterprise/search/search-active-active">}})<br />[JSON]({{<relref "/operate/oss_and_stack/stack-with-enterprise/json">}}) |

1. <a name="enabled-modules-table-note-1"></a>Upgrading existing Active-Active databases to Redis version 8 does not automatically enable these capabilities. Only new Active-Active databases created with Redis version 8 enable these capabilities by default.