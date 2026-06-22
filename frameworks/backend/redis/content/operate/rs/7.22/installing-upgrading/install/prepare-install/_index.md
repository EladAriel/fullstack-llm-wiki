---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/installing-upgrading/install/prepare-install/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Prepare to install Redis Enterprise Software
alwaysopen: false
categories:
- docs
- operate
- rs
description: Prepare to install Redis Enterprise Software.
hideListLinks: true
linkTitle: Prepare to install
weight: 6
url: '/operate/rs/7.22/installing-upgrading/install/prepare-install/'
---

Before you install Redis Enterprise Software:

- [Download an installation package]({{< relref "/operate/rs/7.22/installing-upgrading/install/prepare-install/download-install-package" >}}).

- [View installation questions]({{< relref "/operate/rs/7.22/installing-upgrading/install/manage-installation-questions" >}}) and optionally prepare answers before installation.

- Review the [security considerations]({{< relref "/operate/rs/7.22/security/" >}}) for your deployment.

- Check that you have root-level access to each node, either directly or with `sudo`.

- Check that all [required ports are available]({{< relref "/operate/rs/7.22/installing-upgrading/install/prepare-install/port-availability" >}}).

- [Turn off Linux swap]({{< relref "/operate/rs/7.22/installing-upgrading/configuring/linux-swap.md" >}}) on all cluster nodes.

- If you require the `redislabs` UID (user ID) and GID (group ID) numbers to be the same on all the nodes, create the `redislabs` user and group with the required numbers on each node.

- If you want to use Auto Tiering for your databases, see [Auto Tiering installation]({{< relref "/operate/rs/7.22/installing-upgrading/install/install-on-linux#auto-tiering-installation" >}}).

## Next steps

- View [installation script options]({{< relref "/operate/rs/7.22/installing-upgrading/install/install-script" >}}) before starting the installation.

- [Install Redis Enterprise Software]({{< relref "/operate/rs/7.22/installing-upgrading/install" >}}).
