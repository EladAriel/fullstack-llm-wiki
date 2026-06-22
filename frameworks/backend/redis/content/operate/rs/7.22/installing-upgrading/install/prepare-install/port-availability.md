---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/installing-upgrading/install/prepare-install/port-availability.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Ensure port availability
alwaysopen: false
categories:
- docs
- operate
- rs
description: Make sure required ports are available.
linkTitle: Ensure port availability
weight: 40
url: '/operate/rs/7.22/installing-upgrading/install/prepare-install/port-availability/'
---

Before [installing Redis Enterprise Software]({{< relref "/operate/rs/7.22/installing-upgrading/install" >}}), make sure all required ports are available.

{{<embed-md "port-availability-embed.md">}}

## Update `sysctl.conf` to avoid port collisions

{{<embed-md "port-collision-avoidance.md">}}

## OS conflicts with port 53

{{<embed-md "port-53.md">}}
