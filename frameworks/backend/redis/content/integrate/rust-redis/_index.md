---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/rust-redis/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.150381Z"
---
# _Index

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
