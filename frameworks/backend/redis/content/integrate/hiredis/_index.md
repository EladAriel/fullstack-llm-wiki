---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/hiredis/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.150188Z"
---
# _Index

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
