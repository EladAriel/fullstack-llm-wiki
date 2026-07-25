---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/hiredis/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
LinkTitle: hiredis
Title: C client for Redis
categories:
- docs
- integrate
- oss
- rs
- rc
description: Learn how to build with Redis and C
group: library
stack: true
summary: hiredis is a minimalistic C client library for Redis.
title: hiredis
type: integration
weight: 5
---

Connect your C application to a Redis database using the hiredis client library.

## Overview

hiredis is a minimalistic C client library for Redis that provides a simple, efficient interface for Redis operations. It's designed to be lightweight, fast, and easy to integrate into C applications with minimal dependencies.

## Key Features

- **Lightweight**: Minimal memory footprint and dependencies
- **High Performance**: Optimized for speed and low latency
- **Synchronous & Asynchronous**: Support for both blocking and non-blocking operations
- **Pipeline Support**: Efficient command batching for improved throughput
- **Error Handling**: Comprehensive error reporting and handling
- **Cross-platform**: Works on Linux, macOS, Windows, and embedded systems
- **Thread Safe**: Safe for use in multi-threaded applications
- **Simple API**: Clean, straightforward C interface

## Getting Started

Refer to the complete [C guide]({{< relref "/develop/clients/hiredis" >}}) to install, connect, and use hiredis.
