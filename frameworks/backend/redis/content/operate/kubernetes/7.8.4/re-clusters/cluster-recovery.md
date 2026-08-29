---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/7.8.4/re-clusters/cluster-recovery.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.149448Z"
---
# Cluster Recovery

---
Title: Recover a Redis Enterprise cluster on Kubernetes
alwaysopen: false
categories:
- docs
- operate
- kubernetes
description: This task describes how to recover a Redis Enterprise cluster on Kubernetes.
linkTitle: Recover a Redis cluster
weight: 20
url: '/operate/kubernetes/7.8.4/re-clusters/cluster-recovery/'
---
When a Redis Enterprise cluster loses contact with more than half of its nodes either because of failed nodes or network split,
the cluster stops responding to client connections.
When this happens, you must recover the cluster to restore the connections.

You can also perform cluster recovery to reset cluster nodes, to troubleshoot issues, or in a case of active/passive failover.

The Redis Enterprise for Kubernetes automates these recovery steps:

1. Recreates a fresh Redis Enterprise cluster
1. Mounts the persistent storage with the recovery files from the original cluster to the nodes of the new cluster
1. Recovers the cluster configuration on the first node in the new cluster
1. Joins the remaining nodes to the new cluster.

{{<warning>}}Redis Enterprise for Kubernetes 7.2.4-2 introduces a new limitation. You cannot recover or upgrade your cluster if there are databases with old module versions or manually uploaded modules. See the [Redis Enterprise Software 7.2.4 known limitations]({{< relref "/operate/rs/release-notes/rs-7-2-4-releases/rs-7-2-4-52#cluster-recovery-with-manually-uploaded-modules" >}}) for more details.{{</warning>}}

## Prerequisites

- For cluster recovery, the cluster must be [deployed with persistence]({{< relref "/operate/kubernetes/7.8.4/recommendations/persistent-volumes.md" >}}).

## Recover a cluster

1. Edit the REC resource to set the `clusterRecovery` flag to `true`.

    ```sh
    kubectl patch rec <cluster-name> --type merge --patch '{"spec":{"clusterRecovery":true}}'
    ```


1. Wait for the cluster to recover until it is in the "Running" state.

    To see the state of the cluster, run:

    ```sh
    watch "kubectl describe rec | grep State"
    ```

1. To recover the database, see [Recover a failed database]({{< relref "/operate/rs/databases/recover.md" >}}).
