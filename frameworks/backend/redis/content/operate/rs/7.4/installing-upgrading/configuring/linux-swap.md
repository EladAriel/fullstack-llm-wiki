---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/installing-upgrading/configuring/linux-swap.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Configure swap for Linux
alwaysopen: false
categories:
- docs
- operate
- rs
description: Turn off Linux swap space.
linkTitle: Linux swap configuration
weight: $weight
url: '/operate/rs/7.4/installing-upgrading/configuring/linux-swap/'
---
Linux operating systems use swap space, which is enabled by default, to help manage memory (pages) by
copying pages from RAM to disk. Due to the way Redis Enterprise Software
utilizes and manages memory, it is best to prevent OS swapping. For more details, see [memory limits]({{< relref "/operate/rs/7.4/databases/memory-performance/memory-limit.md" >}}). The
recommendation is to turn off Linux swap completely in the OS.

When you install or build the OS on the machine intended to host your Redis Enterprise Software cluster, avoid configuring swap partitions if possible.

## Turn off swap

To turn off swap in the OS of an existing server, VM, or instance, you
must have `sudo` access or be a root user to run the following commands:

1. Turn off swap:

    ```sh
    sudo swapoff -a
    ```

1. Comment out the swap partitions configured in the OS so swap remains off even after a reboot:

    ```sh
    sudo sed -i.bak '/ swap / s/^(.*)$/#1/g' /etc/fstab
    ```
