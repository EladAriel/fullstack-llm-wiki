---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/databases/connect/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Connect to a database
categories:
- docs
- operate
- rs
description: Learn how to connect your application to a Redis database hosted by Redis
  Enterprise Software and test your connection.
hideListLinks: true
linkTitle: Connect
weight: 20
---

After you [set up a cluster]({{< relref "/operate/rs/clusters/new-cluster-setup" >}}) and [create a Redis database]({{< relref "/operate/rs/databases/create" >}}), you can connect to your database.

To connect to your database, you need the database endpoint, which includes the cluster name (FQDN) and the database port. To view and copy public and private endpoints for a database in the cluster, see the database’s **Configuration > General** section in the Cluster Manager UI.

{{<image filename="images/rs/screenshots/databases/config-general-endpoints.png" width="75%" alt="View public and private endpoints from the General section of the database's Configuration screen." >}}

If you try to connect with the FQDN, and the database does not respond, try connecting with the IP address. If this succeeds, DNS is not properly configured. To set up DNS, see [Configure cluster DNS]({{< relref "/operate/rs/networking/cluster-dns" >}}).

If you want to secure your connection, set up [TLS]({{< relref "/operate/rs/security/encryption/tls/" >}}).

## Connect to a database

Use one of the following connection methods to connect to your database:

- [`redis-cli`]({{< relref "/operate/rs/references/cli-utilities/redis-cli/" >}}) utility

- [Redis Insight](https://redis.com/redis-enterprise/redis-insight/)

- [Redis client]({{< relref "/develop/clients" >}}) for your preferred programming language

For examples, see [Test client connection]({{< relref "/operate/rs/databases/connect/test-client-connectivity" >}}).

## Continue learning with Redis University

See the [Connect to a database on Redis Software](https://university.redis.io/course/zyxx6fdkcm5ahd) for the course.
