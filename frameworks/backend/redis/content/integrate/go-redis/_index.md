---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/go-redis/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.156498Z"
---
# _Index

---
LinkTitle: go-redis
Title: Go client for Redis
categories:
- docs
- integrate
- oss
- rs
- rc
description: Learn how to build with Redis and Go
group: library
stack: true
summary: go-redis is a Go client library for Redis.
title: go-redis
type: integration
weight: 3
---

Connect your Go application to a Redis database using the go-redis client library.

## Overview

go-redis is a type-safe, Redis client library for Go that supports Redis 6.0+ features including Redis Cluster, Redis Sentinel, and Redis streams. It provides a clean, idiomatic Go API for interacting with Redis.

## Key Features

- **Type Safety**: Strongly typed commands and responses
- **Redis Cluster Support**: Built-in support for Redis Cluster deployments
- **Redis Sentinel**: Automatic failover with Redis Sentinel
- **Pipelining**: Efficient command batching for improved performance
- **Pub/Sub**: Real-time messaging with Redis Pub/Sub
- **Streams**: Support for Redis Streams data structure
- **Connection Pooling**: Automatic connection management
- **Context Support**: Full context.Context integration for cancellation and timeouts

## Getting Started

Refer to the complete [Go guide]({{< relref "/develop/clients/go" >}}) to install, connect, and use go-redis with detailed examples and best practices.
