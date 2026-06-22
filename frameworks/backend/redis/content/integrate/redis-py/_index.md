---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/redis-py/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
LinkTitle: redis-py
Title: Python client for Redis
categories:
- docs
- integrate
- oss
- rs
- rc
description: Learn how to build with Redis and Python
group: library
stack: true
summary: redis-py is a Python library for Redis.
title: redis-py
type: integration
weight: 1
---

Connect your Python application to a Redis database using the redis-py client library.

## Overview

redis-py is the recommended Python client for Redis, providing a comprehensive interface for all Redis commands and features. It offers both synchronous and asynchronous APIs, making it suitable for a wide range of Python applications from simple scripts to high-performance web applications.

## Key Features

- **Complete Redis Support**: Full coverage of all Redis commands and data types
- **Async/Await Support**: Native asyncio support for high-performance applications
- **Connection Pooling**: Efficient connection management for multi-threaded applications
- **Redis Cluster**: Built-in support for Redis Cluster deployments
- **Sentinel Support**: High availability with Redis Sentinel integration
- **Pipeline Support**: Command batching for improved performance
- **Pub/Sub**: Real-time messaging with Redis publish/subscribe
- **Framework Integration**: Seamless integration with Django, Flask, FastAPI, and other Python frameworks

## Getting Started

Refer to the complete [Python guide]({{< relref "/develop/clients/redis-py" >}}) to install, connect, and use redis-py.
