---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/rust-redis/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
LinkTitle: rust-redis
Title: Rust client for Redis
categories:
- docs
- integrate
- oss
- rs
- rc
description: Learn how to build with Redis and Rust
group: library
stack: true
summary: redis-rs is a Rust client library for Redis.
title: rust-redis
type: integration
weight: 9
---

Connect your Rust application to a Redis database using the redis-rs client library.

## Overview

redis-rs is a high-performance Redis client for Rust that leverages Rust's memory safety and performance characteristics. It provides both synchronous and asynchronous APIs with excellent integration into the Rust ecosystem.

## Key Features

- **Memory Safety**: Rust's ownership system prevents memory leaks and data races
- **High Performance**: Zero-cost abstractions and efficient memory usage
- **Async Support**: Tokio integration for asynchronous, non-blocking operations
- **Type Safety**: Strong typing with compile-time error checking
- **Connection Pooling**: Efficient connection management for concurrent applications
- **Pipeline Support**: Command batching for improved throughput
- **Cluster Support**: Redis Cluster client for distributed setups
- **Comprehensive API**: Full Redis command coverage with idiomatic Rust interfaces

## Getting Started

Refer to the [Rust Redis documentation](https://docs.rs/redis/latest/redis/) to install, connect, and use redis-rs.
