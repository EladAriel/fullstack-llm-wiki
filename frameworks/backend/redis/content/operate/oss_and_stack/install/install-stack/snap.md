---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/install/install-stack/snap.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.246746Z"
---
# Snap

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

{{< note >}}
If you only need the Redis CLI (`redis-cli`) and not the full Redis Open Source distribution, see [Install redis-cli]({{< relref "/operate/oss_and_stack/install/install-stack/install-redis-cli" >}}).
{{< /note >}}

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
