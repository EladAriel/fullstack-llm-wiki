---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/installing-upgrading/upgrading/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
