---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/clusters/change-node-role.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.432718Z"
---
# Change Node Role

---
Title: Change node roles
alwaysopen: false
categories:
- docs
- operate
- rs
description: Change node roles to demote the primary node to a secondary node or promote a secondary node to become the primary node.
linkTitle: Change node roles
weight: 65
url: '/operate/rs/7.8/clusters/change-node-role/'
---

A Redis Software cluster contains a primary node, which coordinates cluster-wide management operations, and multiple secondary nodes. Nodes with either role can host database shards.

## Demote primary node

To demote the primary node to a secondary node using the Cluster Manager UI:

1. On the **Nodes** screen, click {{< image filename="/images/rs/buttons/button-toggle-actions-vertical.png#no-click" alt="More actions button" width="22px" class="inline" >}} for the primary node you want to demote.

    {{<image filename="images/rs/screenshots/nodes/primary-node-more-actions.png" alt="Click the more actions button for a node to access node actions.">}}

1. Select **Set as a secondary node** from the list.

1. Select one of the options to determine the new primary node:

    - **Automatically**: The cluster decides which node becomes the new primary node.

    - **Choose specific node**: You can manually select which node becomes the new primary node.

    {{<image filename="images/rs/screenshots/nodes/primary-node-set-as-secondary-dialog.png" alt="The Set as a secondary node dialog has two options to select the new primary node, either automatically or manually.">}}

1. Click **Confirm**.

## Promote secondary node

To promote a secondary node to become the primary node using the Cluster Manager UI:

1. On the **Nodes** screen, click {{< image filename="/images/rs/buttons/button-toggle-actions-vertical.png#no-click" alt="More actions button" width="22px" class="inline" >}} for the secondary node you want to promote.

    {{<image filename="images/rs/screenshots/nodes/secondary-nodes-more-actions.png" alt="Click the more actions button for a node to access node actions.">}}

1. Select **Set as the primary node** from the list.

1. Click **Confirm**.

After this node becomes the primary node, all cluster management traffic is directed to it.
