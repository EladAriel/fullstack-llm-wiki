---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/clusters/replace-node.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Replace a cluster node
alwaysopen: false
categories:
- docs
- operate
- rs
description: Replace a node in your cluster that is down.
linkTitle: Replace node
weight: 90
url: '/operate/rs/7.4/clusters/replace-node/'
---
A failed node will appear as `Down` ({{< image filename="/images/rs/icons/node-down-icon.png#no-click" alt="Node down icon" class="inline" >}}) in the **Nodes** list.

To replace a failed node: 

1. Prepare a new node identical to the old one.

1.  Install and
    configure Redis Enterprise Software on the node. See [Install and setup]({{< relref "/operate/rs/7.4/installing-upgrading" >}}) for more information.

    {{< note >}}
If you are using [Auto Tiering]({{< relref "/operate/rs/7.4/databases/auto-tiering/" >}}), make sure the required flash storage is set up on this new node.
    {{< /note >}}

1. [Add the node]({{< relref "/operate/rs/7.4/clusters/add-node" >}}) to the cluster. Make sure the new node has as much available memory as the faulty
    node.

    If the new node does not have enough memory, you will be prompted to add a node with enough memory.

1. A message will appear informing you that the cluster has a faulty node
    and that the new node will replace the faulty node.

    {{< note >}}
- If there is a faulty node in the cluster to which you are adding a node, Redis Enterprise Software will use the new node to replace the faulty one.
- Any existing [DNS records]({{< relref "/operate/rs/7.4/networking/cluster-dns" >}}) must be updated
each time a node is added or replaced.
    {{< /note >}}
