---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/installing-upgrading/install/customize-user-and-group.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Customize system user and group
alwaysopen: false
categories:
- docs
- operate
- rs
description: Specify the user and group who own all Redis Enterprise Software processes.
linkTitle: Customize user and group
weight: 40
url: '/operate/rs/7.22/installing-upgrading/install/customize-user-and-group/'
---

By default, Redis Enterprise Software is installed with the user:group `redislabs:redislabs`.

During installation, you can specify the user and group that own all Redis Enterprise Software processes.

## Considerations

- Custom installation user is supported on Red Hat Enterprise Linux and compatible distributions.

- You must create the user and group before installing Redis Enterprise Software.

- You must install Redis Enterprise Software on all nodes in the cluster with the same user and group.

- You can specify an LDAP user as the installation user.

- If you specify the user only, then installation is run with the primary group that the user belongs to.

## Install with custom user or group

To customize the user or group during [installation]({{< relref "/operate/rs/7.22/installing-upgrading/install/install-on-linux" >}}), include the `--os-user` or `--os-group` [command-line options]({{< relref "/operate/rs/7.22/installing-upgrading/install/install-script" >}}) when you run the `install.sh` script.

```sh
sudo ./install.sh --os-user <user> --os-group <group>
```
