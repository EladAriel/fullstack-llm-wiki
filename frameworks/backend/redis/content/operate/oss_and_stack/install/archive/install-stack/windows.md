---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/install/archive/install-stack/windows.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
categories:
- docs
- operate
- stack
- oss
description: How to install Redis Stack on Windows
linkTitle: Windows
title: Install Redis Stack on Windows
weight: 3
---

## Run Redis on Windows using Memurai

Redis is now natively supported on Windows through [Memurai](https://www.memurai.com/), the official Redis partner for Windows compatibility.

## Run Redis on Windows using Docker

To install Redis Stack on Windows, you will need to have Docker installed. When Docker is up and running, open Windows PowerShell and follow the instructions described in [Run Redis Stack on Docker]({{< relref "/operate/oss_and_stack/install/install-stack/docker" >}}). Then, use Docker to connect with `redis-cli` as explained in that topic.

{{% alert title="About using WSL and Ubuntu for Windows " color="warning" %}}
If you attempt to use Windows Subsystem for Linux (WSL) or Ubuntu for Windows to follow [Linux instructions]({{< relref "/operate/oss_and_stack/install/install-stack/apt" >}}), you will get a `systemd` error telling you `System has not been booted with systemd as init system (PID 1). Can't operate.` Do not fret. Just use Docker. 

_`systemd` is a suite of basic building blocks for a Linux system._ For more information about its function, see [System and Service Manager](https://systemd.io/). This becomes an issue due to the lack of support for Linux workflows on WSL. But, you can test the instructions listed in [Systemd support is now available in WSL!](https://devblogs.microsoft.com/commandline/systemd-support-is-now-available-in-wsl/). Let us know how that worked for you. 
{{% /alert %}}

