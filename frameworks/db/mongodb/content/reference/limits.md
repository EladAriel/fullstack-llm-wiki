---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/limits.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# MongoDB Limits and Thresholds

This document provides a collection of hard and soft limitations of the MongoDB system. The limitations on this page apply to deployments hosted in Atlas and self-hosted MongoDB deployments, unless specified otherwise.

## {+atlas+} Limitations

The following limitations apply only to deployments hosted in {+atlas+}. If any of these limits present a problem for your organization, contact :atlas:`Atlas support </support>`.

### {+atlas+} Cluster Limits

### {+atlas+} Connection Limits and Cluster Tier

{+atlas+} limits concurrent incoming connections based on the cluster tier and `class <storage-class-ui>`. {+atlas+} connection limits apply per node. For sharded clusters, {+atlas+} connection limits apply per `mongos <sharding-read-operations>` router. The number of `mongos <sharding-read-operations>` routers is equal to the number of replica set nodes across all shards.

Your :manual:`read preference </core/read-preference/>` also contributes to the total number of connections that {+atlas+} can allocate for a given query.

{+atlas+} has the following connection limits for the specified cluster tiers:

> **Note:** {+atlas+} reserves a small number of connections to each cluster for
supporting {+atlas+} services.

### {+atlas+} Multi-Cloud Connection Limitation

If you're connecting to a multi-cloud {+atlas+} deployment through a `private connection <conn-string-options>`, you can access only the nodes in the same cloud provider that you're connecting from. This cloud provider might not have the `primary` node in its region. When this happens, you must specify the `secondary read preference <read-preference>` mode in the connection string to access the deployment.

If you need access to all nodes for your multi-cloud {+atlas+} deployment from your current provider through a private connection, you must perform one of the following actions:

- Configure a VPN in the current provider to each of the remaining
providers.

- Configure a `private endpoint <private-endpoint>` to {+atlas+}
for each of the remaining providers.

### {+atlas+} Collection and Index Limits

While there is no hard limit on the number of collections in a single {+atlas+} cluster, the performance of a cluster might degrade if it serves a large number of collections and indexes. Larger collections have a greater impact on performance.

The recommended maximum combined number of collections and indexes by {+atlas+} cluster tier are as follows:

### {+atlas+} Organization and Project Limits

{+atlas+} deployments have the following organization and project limits:

### {+atlas+} Service Account Limits

{+atlas+} service accounts have the following organization and project limits:

### {+atlas+} Label Limits

{+atlas+} limits the length and enforces ReGex requirements for the following component labels:

<atlas-faq-azure-gcp-peering-only>`, the cluster name character limit is 23.

These characters must be unique within the cluster's project. Cluster names with fewer than 23 characters can't end with a hyphen (`-`). Cluster names with more than 23 characters can't have a hyphen as the 23rd character.

number plus the following punctuation: `-_.(),:&@+'`.

### Free Cluster, and Flex Cluster Limitations

Additional limitations apply to {+atlas+} free clusters, and {+flex-clusters+}. To learn more, see the following resources:

- :atlas:`Atlas Free Cluster Limitations </reference/free-shared-limitations>`
- :atlas:`{+atlas-flex+} Limitations </reference/flex-limitations>`
### {+atlas+} Command Limitations

Some MongoDB commands are unsupported in {+atlas+}. Additionally, some commands are supported only in {+atlas+} free clusters. To learn more, see the following resources:

- :atlas:`Unsupported Commands in Atlas </unsupported-commands>`
- :atlas:`Commands Available Only in Free Clusters
</free-tier-commands>`

## Collection and Database Size Limits

MongoDB does not impose a hard limit on collection or database sizes. The maximum size of a collection or database depends on the file system of the host server. For example:

- **ext4**: Maximum file size of 16 tebibytes (TiB).
- **XFS**: Maximum file size of 8 exbibytes (EiB).
To scale beyond file system or hardware limits, MongoDB offers strategies such as `sharding <sharding-sharded-cluster>`, which allows collections to grow indefinitely. For collections nearing these limits or performance bottlenecks, MongoDB recommends sharding or migrating to a clustered setup such {+atlas+}, which supports auto-scaling.

### Sharding and Initial Size

When sharding a collection, MongoDB determines initial chunk ranges based on the shard key and splits your data into manageable chunks. These limits only affect the initial sharding operation:

- `chunkSize` (default: 128 MB).
- Average Shard Key Size (typical size is 16 bytes).
## BSON Documents

## Naming Restrictions

## Naming Warnings

> **Warning:** Use caution, the issues discussed in this section could lead to data
loss or corruption.

### MongoDB does not support duplicate field names

.. include:: /includes/warning-document-duplicate-key-names-body.rst

### Avoid Ambiguous Field Names

.. include:: /includes/warning-ambiguous-field-names.rst

### Import and Export Concerns With Dollar Signs (`$`) and Periods (`.`)

.. include:: /includes/warning-dot-dollar-import-export-body.rst

### Possible Data Loss With Dollar Signs (`$`) and Periods (`.`)

.. include:: /includes/warning-possible-data-loss-body.rst

## Namespaces

## Indexes

## Sorts

## Data

## Replica Sets

## Sharded Clusters

Sharded clusters have the restrictions and thresholds described here.

### Sharding Operational Restrictions

### Shard Key Limitations

## Operations

## Sessions
