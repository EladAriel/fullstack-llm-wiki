---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/installing-upgrading/install/offline-installation.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Offline installation
alwaysopen: false
categories:
- docs
- operate
- rs
description: If you install Redis Software on a machine with no internet
  connection, you need to perform two tasks manually.
linkTitle: Offline installation
weight: 60
---
By default, the installation process requires an internet connection to
enable installing dependency packages and for [synchronizing the
operating system clock]({{< relref "/operate/rs/clusters/configure/sync-clocks.md" >}}) against an NTP server.

If you install Redis Software on a machine without an
internet connection, you need to perform two tasks manually.

## Install required dependency packages

When you install Redis Software on a machine that is not connected to the internet, the installation process fails and displays an error message informing you it failed to automatically install dependencies. Review the installation steps in the console to see which missing dependencies the process attempted to install. Install all these dependency packages and then run the installation again.

## Set up NTP time synchronization

At the end of the installation, the process asks if you want to set up NTP time synchronization. If you choose `Yes` while you are not connected to the internet, the action fails and displays the appropriate error message, but the installation completes successfully. Despite the successful completion of the installation, you still have to configure all nodes for [NTP time synchronization]({{< relref "/operate/rs/clusters/configure/sync-clocks.md" >}}).
