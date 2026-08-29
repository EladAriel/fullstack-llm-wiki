---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/installing-upgrading/upgrading/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.733714Z"
---
# _Index

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
