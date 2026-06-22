---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/bdb/probabilistic.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Probabilistic data structures configuration object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Configuration object for probabilistic data structures
linkTitle: probabilistic
weight: $weight
---

Configuration fields for probabilistic data structures.

| Field | Type/Value | Description |
|-------|------------|-------------|
| bf-error-rate | number (range: 0-1) (default: 0.01) | Error ratio for new Bloom filters. These defaults are applied to each new Bloom filter upon its creation. |
| bf-initial-size | integer (range: 1-1048576) (default: 100) | Initial capacity for new Bloom filters. These defaults are applied to each new Bloom filter upon its creation. |
| bf-expansion-factor | integer (range: 0-32768) (default: 2) | Expansion factor for new Bloom filters. These defaults are applied to each new Bloom filter upon its creation. |
| cf-initial-size | integer (range: 1-1048576) (default: 1024) | Initial capacity for new Cuckoo filters. These defaults are applied to each new Cuckoo filter upon its creation. |
| cf-bucket-size | integer (range: 1-255) (default: 2) | Number of items in each bucket for new Cuckoo filters. These defaults are applied to each new Cuckoo filter upon its creation. |
| cf-max-iterations | integer (range: 1-65535) (default: 20) | Maximum iterations for new Cuckoo filters. These defaults are applied to each new Cuckoo filter upon its creation. |
| cf-expansion-factor | integer (range: 0-32768) (default: 1) | Expansion factor for new Cuckoo filters. These defaults are applied to each new Cuckoo filter upon its creation. |
| cf-max-expansions | integer (range: 1-65536) (default: 32) | Maximum expansions for new Cuckoo filters. These defaults are applied to each new Cuckoo filter upon its creation. |
