---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/install/install-stack/rpm.md"
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
description: How to install Redis Open Source using RPM
linkTitle: RPM
title: Install Redis Open Source on Linux
weight: 3
---

## Install Redis Open Source on Rocky Linux 8 and 9, or AlmaLinux 8 and 9 using RPM

Follow these steps to install Redis Open Source.

1. Create the file `/etc/yum.repos.d/redis.repo` with the following contents.

    - For Rocky Linux 9 and AlmaLinux 9
    {{< highlight ini >}}
    [Redis]
    name=Redis
    baseurl=http://packages.redis.io/rpm/rockylinux9
    enabled=1
    gpgcheck=1
    {{< /highlight >}}

    - For Rocky Linux 8 and AlmaLinux 8
    {{< highlight ini >}}
    [Redis]
    name=Redis
    baseurl=http://packages.redis.io/rpm/rockylinux8
    enabled=1
    gpgcheck=1
    {{< /highlight >}}

2. Run the following commands:

    {{< highlight bash >}}
    curl -fsSL https://packages.redis.io/gpg > /tmp/redis.key
    sudo rpm --import /tmp/redis.key
    sudo yum install redis
    {{< / highlight >}}

Redis will not start automatically, nor will it start at boot time. To do this, run the following commands.

{{< highlight bash >}}
sudo systemctl enable redis
sudo systemctl start redis
{{< /highlight >}}
