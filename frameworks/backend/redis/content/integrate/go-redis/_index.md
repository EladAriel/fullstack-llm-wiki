---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/go-redis/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
