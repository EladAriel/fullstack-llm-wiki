---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/jedis/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.153792Z"
---
# _Index

---
LinkTitle: jedis
Title: Java client for Redis
categories:
- docs
- integrate
- oss
- rs
- rc
description: Learn how to build with Redis and Java
group: library
stack: true
summary: jedis is a Java library for Redis.
title: jedis
type: integration
weight: 2
---

Connect your Java application to a Redis database using the Jedis client library.

## Overview

Jedis is a popular Java client for Redis that provides a simple, synchronous interface for Redis operations. It offers comprehensive Redis command support and is widely used in Java applications for its straightforward API and reliable performance.

## Key Features

- **Synchronous Operations**: Simple, blocking API that's easy to understand and use
- **Complete Redis Support**: Full coverage of all Redis commands and data types
- **Connection Pooling**: Built-in connection pool management for multi-threaded applications
- **Redis Cluster**: Native support for Redis Cluster deployments
- **Sentinel Support**: High availability with Redis Sentinel integration
- **Pipeline Support**: Command batching for improved performance
- **Pub/Sub**: Real-time messaging with Redis publish/subscribe
- **Thread Safety**: Safe connection pooling for concurrent Java applications

## Getting Started

Refer to the complete [Jedis guide]({{< relref "/develop/clients/jedis" >}}) to install, connect, and use Jedis.
