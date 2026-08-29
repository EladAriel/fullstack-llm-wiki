---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/installing-upgrading/install/prepare-install/port-availability.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.360064Z"
---
# Port Availability

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
