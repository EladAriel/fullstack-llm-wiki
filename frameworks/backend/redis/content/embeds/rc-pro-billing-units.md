---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-pro-billing-units.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

The Redis Billing Unit types associated with your Pro subscription depend on your database memory size and throughput requirements.

| Billing unit type | Capacity (Memory/Throughput) |
|:------------|:----------|
| Pico | 100MB / 100 ops/sec |
| Nano | 500MB / 500 ops/sec |
| Micro | 1GB / 1K ops/sec |
| High-throughput | 2.5GB / 25K ops/sec |
| Small | 12.5GB / 12.5K ops/sec |
| Large | 25GB  / 25K ops/sec |
| Very large<sup>[1](#table-note-1)</sup> | 50GB / 5K ops/sec |
| XLarge<sup>[2](#table-note-2)</sup> | 50GB / 10K ops/sec |
| Flex-10<sup>[3](#table-note-3)</sup> | 50GB / 5K ops/sec |
| Flex-20<sup>[3](#table-note-3)</sup> | 50GB / 10K ops/sec |
| Flex-30<sup>[3](#table-note-3)</sup> | 50GB / 15K ops/sec |
| Flex-40<sup>[3](#table-note-3)</sup> | 50GB / 20K ops/sec |
| Flex-50<sup>[3](#table-note-3)</sup> | 50GB / 25K ops/sec |

1. <a name="table-note-1" style="display: block; height: 80px; margin-top: -80px;"></a>Used for databases with Auto Tiering before Redis 7.2.

2. <a name="table-note-2" style="display: block; height: 80px; margin-top: -80px;"></a>Used for hosted databases with Auto Tiering between Redis 7.2 and Redis 8.2. 

3. <a name="table-note-3" style="display: block; height: 80px; margin-top: -80px;"></a>Used for Redis Flex databases for Redis 8.2 or later. Available Flex billing units depend on the RAM percentage you set for your database.

Prices vary according to the cloud provider and region.  Minimum prices apply.