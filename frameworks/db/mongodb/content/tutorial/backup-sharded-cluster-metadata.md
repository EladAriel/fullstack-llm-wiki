---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/backup-sharded-cluster-metadata.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================================

# Back Up Self-Managed Cluster Metadata

This procedure shuts down the :binary:`~bin.mongod` instance of a `config server <sharding-config-server>` in order to create a backup of a `sharded cluster's <sharding-sharded-cluster>` metadata. The cluster's config servers store all of the cluster's metadata, most importantly the mapping from `chunks <chunk>` to `shards <shard>`.

When you perform this procedure, the cluster remains operational [#read-only]_.

#. Disable the cluster balancer process temporarily. See `sharding-balancing-disable-temporarily` for more information.

#. Shut down one of the config databases.

#. Create a full copy of the data files (i.e. the path specified by the :setting:`~storage.dbPath` option for the config instance.)

#. Restart the original configuration server.

#. Re-enable the balancer to allow the cluster to resume normal balancing operations. See the `sharding-balancing-disable-temporarily` section for more information on managing the balancer process.

> **Seealso:** `/core/backups`

the cluster cannot split any chunks nor can it migrate chunks between shards. Your application will be able to write data to the cluster. See `sharding-config-server` for more information.
