---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/databases/create-database/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Create a database
alwaysopen: false
categories:
- docs
- operate
- rc
description: null
hideListLinks: true
linkTitle: Create database
weight: 10
---

A database is the heart of any Redis Cloud deployment. 

The process for Creating a database depends on the type of [subscription plan]({{< relref "/operate/rc/subscriptions" >}}) you need.

An **Essentials** plan is a fixed monthly price for a single database. It is cost-efficient and designed for low-throughput scenarios. It supports a range of availability, persistence, and backup options. Pricing supports low throughput workloads.
- [Create an Essentials database]({{< relref "/operate/rc/databases/create-database/create-essentials-database" >}})
- [Create a Redis Flex database]({{< relref "/operate/rc/databases/create-database/create-flex-database" >}})

A **Free** plan is a type of Essentials plan designed for learning and building test projects. It gives you enough space to learn Redis concepts and develop application prototypes. You can upgrade to a paid Essentials plan at any time.
- [Create a free database]({{< relref "/operate/rc/databases/create-database/create-free-database" >}})

A **Pro** plan is an hourly price based on capacity. It supports more databases, larger databases, greater throughput, and unlimited connections. 
- [Create a Pro database with a new subscription]({{< relref "/operate/rc/databases/create-database/create-pro-database-new" >}})
- [Create a Pro database in an existing subscription]({{< relref "/operate/rc/databases/create-database/create-pro-database-existing" >}})
- [Create an Active-Active database]({{< relref "/operate/rc/databases/active-active/create-active-active-database" >}})


