---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/installing-upgrading/install/install-script.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.552317Z"
---
# Install Script

---
Title: Installation script command-line options
alwaysopen: false
categories:
- docs
- operate
- rs
description: Command-line options for the install.sh script.
linkTitle: Installation script options
weight: 20
---

Run `./install.sh --help` to view command-line options supported by the installation script.

The following options are supported:

| Option | Description |
|--------|-------------|
| `-y` | Automatically answers `yes` to all install prompts, accepting all default values<br/>See [Manage install questions]({{< relref "/operate/rs/installing-upgrading/install/manage-installation-questions" >}})|
| <nobr>`-c <answer file>`</nobr> | Specify answer file used to respond to install prompts<br/>See [Manage install questions]({{< relref "/operate/rs/installing-upgrading/install/manage-installation-questions" >}})|
| <nobr>`-s <socket dir>`</s> | Specify directory for redislabs unix sockets  _(new installs only)_|
| <nobr>`--install-dir <dir>`</nobr> | Specifies installation directory _(new installs only)_ <br/> See [Customize install locations]({{< relref "/operate/rs/installing-upgrading/install/customize-install-directories" >}})|  
| <nobr>`--config-dir <dir>` | Configuration file directory *(new installs only)* <br/>See [Customize install locations]({{< relref "/operate/rs/installing-upgrading/install/customize-install-directories" >}})|
| <nobr>`--var-dir <dir>`</nobr> | Var directory used for installation *(new installs only)* <br/>See [Customize install locations]({{< relref "/operate/rs/installing-upgrading/install/customize-install-directories" >}})|
| <nobr>`--os-user <user>`| Operating system user account associated with install; default: `redislabs`<br/>See [Customize user and group]({{< relref "/operate/rs/installing-upgrading/install/customize-user-and-group" >}}) *(new installs only)*|
|<nobr>`--os-group <group>` | Operating system group associated with install; default: `redislabs`<br/>See [Customize user and group]({{< relref "/operate/rs/installing-upgrading/install/customize-user-and-group" >}}) *(new installs only)* |
| `--skip-dns-port-verification` | Skip DNS port verification during installation |
| <nobr>`--update-env-path`</nobr> | Add paths related to Redis Software to root's PATH environment variable<br/>See [Manage install questions]({{< relref "/operate/rs/installing-upgrading/install/manage-installation-questions" >}}) |
