---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-change-a-shard-key.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================

# Change a Shard Key

The ideal shard key allows MongoDB to distribute documents evenly throughout the cluster while facilitating common query patterns. A suboptimal shard key can lead to uneven data distribution and the following problems:

- `Jumbo chunks <sharding-troubleshooting-jumbo-chunks>`
- :ref:`Uneven load distribution
<sharding-troubleshooting-monotonicity>`

- :ref:`Decreased query performance over time
<sharding-troubleshooting-scatter-gather>`

To address these issues, MongoDB allows you to change your shard key:

- You can `refine a shard key <shard-key-refine>` by adding a suffix
field or fields to the existing shard key.

- You can change a collection's shard key entirely and :ref:`reshard a collection
<sharding-resharding>`.

Data distribution fixes are most effective when you reshard a collection. If you want to improve data distribution and your cluster meets the `criteria to reshard <reshard-requirements>`, you should reshard the collection instead of refining the shard key. If your cluster doesn't meet the criteria to reshard, you should refine the shard key.

For more information on common performance and scaling issues and advice on how to fix them, read `shardkey-troubleshoot-shard-keys`.

## Contents

- Refine a Shard Key </core/sharding-refine-a-shard-key.txt>
- Reshard a Collection </core/sharding-reshard-a-collection.txt>
