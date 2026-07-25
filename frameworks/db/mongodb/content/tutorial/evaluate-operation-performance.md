---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/evaluate-operation-performance.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================

# Analyze Query Performance

MongoDB provides several ways to examine the performance of your workload, allowing you to understand query performance and identify long-running queries. Understanding query performance helps you build effective indexes and ensure your application runs critical queries efficiently.

## Identify Slow Queries

Use the following methods to identify slow queries that occur on your deployment.

### Performance Overview

The following methods provide overviews of your deployment's performance. Use these methods to determine if there are performance issues that need to be addressed:

### Analyze a Slow Query

Use these methods to analyze a slow query and determine the cause of poor performance:

## Perform Advanced Query Analysis

The following methods are suited for deeper investigation of problematic queries, and can provide fine-grained performance insights:

## Contents

- Explain Results </reference/explain-results>
- Database Profiler </tutorial/manage-the-database-profiler>
- Monitor Slow Queries </tutorial/monitor-slow-queries>
- Block Slow Queries </tutorial/operation-rejection-filters>
- Troubleshoot Slow Queries in Production </troubleshooting/slow-queries-in-production>
