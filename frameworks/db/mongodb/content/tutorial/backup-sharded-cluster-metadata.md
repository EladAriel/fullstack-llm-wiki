---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/backup-sharded-cluster-metadata.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.569066Z"
---
.. _back-up-sharded-cluster-metadata:

# Back Up Self-Managed Cluster Metadata

**meta:** :keywords: on-prem
   :description: Create a backup of a sharded cluster's metadata by temporarily disabling the balancer and copying config server data files.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

This procedure shuts down the :binary:`~bin.mongod` instance of a
:ref:`config server <sharding-config-server>` in order to create a
backup of a :ref:`sharded cluster's <sharding-sharded-cluster>`
metadata. The cluster's config servers store all of the cluster's
metadata, most importantly the mapping from :term:`chunks <chunk>` to
:term:`shards <shard>`.

When you perform this procedure, the cluster remains operational
[#read-only]_.

#. Disable the cluster balancer process temporarily. See
   :ref:`sharding-balancing-disable-temporarily` for more information.

#. Shut down one of the config databases.

#. Create a full copy of the data files (i.e. the path specified by
   the :setting:`~storage.dbPath` option for the config instance.)

#. Restart the original configuration server.

#. Re-enable the balancer to allow the cluster to resume normal
   balancing operations. See the
   :ref:`sharding-balancing-disable-temporarily` section for more
   information on managing the balancer process.

**seealso:** :doc:`/core/backups`


.. [#read-only] While one of the three config servers is unavailable,
   the cluster cannot split any chunks nor can it migrate chunks
   between shards. Your application will be able to write data to the
   cluster. See :ref:`sharding-config-server` for more information.