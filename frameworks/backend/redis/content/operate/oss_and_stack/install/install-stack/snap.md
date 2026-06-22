---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/install/install-stack/snap.md"
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
description: How to install Redis Open Source using Snap
linkTitle: Snap
title: Install Redis Open Source on Linux
weight: 4
---

## Install Redis Open Source on Ubuntu Linux using Snap

To install Redis via snap, run the following commands:

{{< highlight bash >}}
sudo apt update
sudo apt install redis-tools # this will install `redis-cli`
sudo snap install redis
{{< / highlight >}}

Redis will start automatically after installation and also at boot time.

## Connect to Redis

Once Redis is running, you can test it by running `redis-cli`:

{{< highlight bash  >}}
redis-cli
{{< / highlight >}}

Test the connection with the `ping` command:

{{< highlight bash  >}}
127.0.0.1:6379> PING
PONG
{{< / highlight >}}
