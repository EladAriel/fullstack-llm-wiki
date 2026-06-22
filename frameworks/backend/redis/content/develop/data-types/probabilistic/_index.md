---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/data-types/probabilistic/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
aliases:
- /data-types/probabilistic/
- /manual/data-types/probabilistic/
categories:
- docs
- develop
- stack
- oss
- rs
- rc
- oss
- kubernetes
- clients
description: Probabilistic data structures in Redis
linkTitle: Probabilistic
title: Probabilistic
weight: 80
---

*Probabilistic data structures* give approximations of statistics such as
counts, frequencies, and rankings rather than precise values.
The advantage of using approximations is that they are adequate for
many common purposes but are much more efficient to calculate. They
sometimes have other advantages too, such as obfuscating times, locations,
and other sensitive data.

Probabilistic data structures are available as part of Redis Open Source and they are available in Redis Software and Redis Cloud.
See
[Install Redis Open Source]({{< relref "/operate/oss_and_stack/install/install-stack" >}}) or
[Install Redis Software]({{< relref "/operate/rs/installing-upgrading/install" >}})
for full installation instructions.