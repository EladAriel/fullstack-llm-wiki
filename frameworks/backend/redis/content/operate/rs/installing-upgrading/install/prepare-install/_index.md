---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/installing-upgrading/install/prepare-install/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Prepare to install Redis Software
alwaysopen: false
categories:
- docs
- operate
- rs
description: Prepare to install Redis Software.
hideListLinks: true
linkTitle: Prepare to install
weight: 6
---

Before you install Redis Software:

- [Download an installation package]({{< relref "/operate/rs/installing-upgrading/install/prepare-install/download-install-package" >}}).

- [View installation questions]({{< relref "/operate/rs/installing-upgrading/install/manage-installation-questions" >}}) and optionally prepare answers before installation.

- Review the [security considerations]({{< relref "/operate/rs/security/" >}}) for your deployment.

- Check that you have root-level access to each node, either directly or with `sudo`.

- Check that all [required ports are available]({{< relref "/operate/rs/installing-upgrading/install/prepare-install/port-availability" >}}).

- [Turn off Linux swap]({{< relref "/operate/rs/installing-upgrading/configuring/linux-swap.md" >}}) on all cluster nodes.

- If you require the `redislabs` UID (user ID) and GID (group ID) numbers to be the same on all the nodes, create the `redislabs` user and group with the required numbers on each node.

- If you want to use Auto Tiering for your databases, see [Auto Tiering installation]({{< relref "/operate/rs/installing-upgrading/install/install-on-linux#auto-tiering-installation" >}}).

## Next steps

- View [installation script options]({{< relref "/operate/rs/installing-upgrading/install/install-script" >}}) before starting the installation.

- [Install Redis Software]({{< relref "/operate/rs/installing-upgrading/install" >}}).
