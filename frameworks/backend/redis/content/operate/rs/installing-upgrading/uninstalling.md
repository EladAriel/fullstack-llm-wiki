---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/installing-upgrading/uninstalling.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
LinkTitle: Uninstall
Title: Uninstall Redis Software
alwaysopen: false
categories:
- docs
- operate
- rs
description: null
weight: 70
---

Use the script `rl_uninstall.sh` to uninstall Redis Software and remove its files from a node. The script also deletes all Redis data and configuration from the node.

The uninstall script does not remove the node from the cluster, but the node's status changes to down. For node removal instructions, see [Remove a cluster node]({{<relref "/operate/rs/clusters/remove-node">}}).

## Uninstall Redis Software

To uninstall Redis Software from a cluster node:

1. Navigate to the script's location, which is in `/opt/redislabs/bin/` by default.

1. Run the uninstall script as the root user:

    ```sh
    sudo ./rl_uninstall.sh
    ```

When you run the uninstall script on a node, it only uninstalls Redis Software from that node. To uninstall Redis Software for the entire cluster, run the uninstall script on each cluster node.
