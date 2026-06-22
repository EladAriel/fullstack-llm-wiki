---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/connection-pool-overview.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Connection Pool Overview

This document describes how to use a connection pool to manage connections between applications and MongoDB instances.

## What is a Connection Pool?

### Definition

A connection pool is a cache of open, ready-to-use database connections maintained by the :driver:`driver </>`. Your application can get connections from the pool, perform operations, and return connections to the pool. Connection pools are thread-safe.

### Benefits of a Connection Pool

A connection pool reduces application latency and the number of new connections created. The pool creates connections at startup, and connections return to the pool automatically — applications do not need to return them manually. Some connections are active and some are available. If your application requests a connection and one is available in the pool, a new connection does not need to be created.

## Create and Use a Connection Pool

### Use an Instance of Your Driver's `MongoClient` Object

Most :driver:`drivers </>` provide an object of type `MongoClient`.

Use one `MongoClient` instance per application unless the application is connecting to many separate clusters. Each `MongoClient` instance manages its own connection pool to the MongoDB cluster or node specified when the `MongoClient` is created. `MongoClient` objects are thread-safe in most drivers.

> **Note:** Store your `MongoClient` instance in a place that is globally
available to your application.

### Authentication

To use a connection pool with LDAP, see `LDAP Connection Pool Behavior <ldap-connection-pool-behavior>`.

## Sharded Cluster Connection Pooling

:binary:`~bin.mongos` routers have connection pools for each node in the cluster. The availability of connections to individual nodes within a sharded cluster affects latency. Operations must wait for a connection to be established.

## Connection Pool Configuration Settings

You can specify connection pool settings in these locations:

- The `MongoDB URI <mongodb-uri>`
- Your application's `MongoClient` instance
- Your application framework's configuration files
### Settings

## Contents

- Tuning </tutorial/connection-pool-performance-tuning>
