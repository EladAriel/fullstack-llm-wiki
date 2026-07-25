---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/installing-upgrading/upgrading/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Upgrade an existing Redis Enterprise Software deployment
alwaysopen: false
categories:
- docs
- operate
- rs
description: null
hideListLinks: true
linkTitle: Upgrade
weight: 60
url: '/operate/rs/7.4/installing-upgrading/upgrading/'
---
To upgrade Redis Enterprise Software:

1. Verify appropriate [network ports]({{< relref "/operate/rs/7.4/networking/port-configurations.md" >}}) are either open or used by Redis Enterprise Software.

1. [Upgrade the software on all nodes of the cluster.]({{< relref "/operate/rs/7.4/installing-upgrading/upgrading/upgrade-cluster" >}})

2. _(Optional)_ [Upgrade each database]({{< relref "/operate/rs/7.4/installing-upgrading/upgrading/upgrade-database" >}}) in the cluster or [upgrade an Active-Active database]({{< relref "/operate/rs/7.4/installing-upgrading/upgrading/upgrade-active-active" >}}) to enable new features and important fixes.
