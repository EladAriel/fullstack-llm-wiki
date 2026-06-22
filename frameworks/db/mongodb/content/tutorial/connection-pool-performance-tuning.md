---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/connection-pool-performance-tuning.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Tuning Your Connection Pool Settings

> **Warning:** Do not use :urioption:`socketTimeoutMS` to prevent long-running
server operations. Instead, use :method:`~cursor.maxTimeMS` with
queries so that the server can cancel long-running operations.

### Calculate Maximum Number of Connections

Calculate usage to find the number of operations running for each connection.

Consider four application servers connecting to a replica set with three members. In this scenario, each of the four application servers creates a connection pool for each replica set member.

Calculate the maximum number of connections that are opened by each application server by multiplying :urioption:`maxPoolSize` by the number of members.

Calculate outgoing connections from an application to a three-member replica set:

**100** (:urioption:`maxPoolSize` default `100`) x **3** (replica set members) = **300** (outgoing connections from the application).

Calculate incoming connections from four application servers to a replica set:

**100** (:urioption:`maxPoolSize` default `100`) x **4** (application servers) = **400** (incoming connections to each mongod).
