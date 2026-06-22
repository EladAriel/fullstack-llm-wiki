---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/installing-upgrading/install/install-script.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
