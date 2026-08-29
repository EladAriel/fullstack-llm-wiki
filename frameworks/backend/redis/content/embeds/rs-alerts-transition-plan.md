---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rs-alerts-transition-plan.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.094324Z"
---
# Rs Alerts Transition Plan

| Cluster manager alert | Equivalent PromQL | Description |
|-----------------------|-------------------|-------------|
| BdbSizeAlert | <span class="break-all">`sum by(db, cluster) (redis_server_used_memory) / sum by(db, cluster) (redis_server_maxmemory) > 0.8`</span> | Redis server memory usage exceeds 80% |
| NodeMemoryAlert | <span class="break-all">`(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes > 0.7`</span> | Node memory usage exceeds 70% |
| NodeFreeFlashAlert | <span class="break-all">`(node_available_flash_bytes - node_bigstore_free_bytes) / node_available_flash_bytes > 0.7`</span> | Node flash storage usage exceeds 70% |
| NodeEphemeralStorageAlert | <span class="break-all">`(node_ephemeral_storage_avail_bytes - node_ephemeral_storage_free_bytes) / node_ephemeral_storage_avail_bytes > 0.7`</span> | Node ephemeral storage usage exceeds 70% |
| NodePersistentStorageAlert | <span class="break-all">`(node_persistent_storage_avail_bytes - node_persistent_storage_free_bytes) / node_persistent_storage_avail_bytes > 0.7`</span> | Node persistent storage usage exceeds 70% |
