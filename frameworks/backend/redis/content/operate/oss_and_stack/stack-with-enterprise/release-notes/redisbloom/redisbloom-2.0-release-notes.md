---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-2.0-release-notes.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
LinkTitle: v2.0 (June 2019)
Title: RedisBloom 2.0 release notes
alwaysopen: false
categories:
- docs
- operate
- stack
description: Added more probabilistic data structures, including top-K and count-min
  sketch.
min-version-db: 4.0.0
min-version-rs: 5.0.0
weight: 98
---
## Requirements

RedisBloom v2.0.3 requires:

- Minimum Redis compatibility version (database): 4.0.0
- Minimum Redis Enterprise Software version (cluster): 5.0.0

## v2.0.3 (July 2019)

- Performance improvements:
    - #[95](https://github.com/RedisBloom/RedisBloom/issues/95) Top-K - Reduce checks on heap, now only checks if item count is larger than minimum in heap.
    - #[95](https://github.com/RedisBloom/RedisBloom/issues/95) Top-K - The power of decay was calculated every time. Changed to use a lookup table.
- Major bug fix:
    - #[88](https://github.com/RedisBloom/RedisBloom/issues/88) Replication available for newly added Top-K and Count-min sketch
- Minor bug fixes:
    - #[89](https://github.com/RedisBloom/RedisBloom/issues/89) Module update broke rdb files
    - #[98](https://github.com/RedisBloom/RedisBloom/issues/98) Compilation for macOS

## v2.0.0 (June 2019)

We are proud to announce that we doubled the number of probabilistic data structures that are generally available in RedisBloom.  Full documentation is available on [redisbloom.io](https://redisbloom.io)

- #[70](https://github.com/RedisBloom/RedisBloom/issues/70) Top-K
    - [Commands]({{<relref "/develop/data-types/probabilistic/top-k">}})
    - [Algorithm](https://www.usenix.org/conference/atc18/presentation/gong)

- #[65](https://github.com/RedisBloom/RedisBloom/issues/65) Count-min Sketch
    - [Commands]({{<relref "/develop/data-types/probabilistic/count-min-sketch">}})
    - [Algorithm](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch)
