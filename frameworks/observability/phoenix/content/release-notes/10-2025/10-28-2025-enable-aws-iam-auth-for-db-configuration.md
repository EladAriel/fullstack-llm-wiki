---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/10-2025/10-28-2025-enable-aws-iam-auth-for-db-configuration.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.861392Z"
---
# 10 28 2025 Enable Aws Iam Auth For Db Configuration

---
title: "10.28.2025: Enable AWS IAM Auth for DB Configuration"
description: Available in Phoenix 12.9+
---

Added support for **AWS IAM–based authentication** for PostgreSQL connections to **AWS Aurora and RDS**. This enhancement enables the use of **short-lived IAM tokens** instead of static passwords, improving security and compliance for database access.

<Card title="Pull Request #9936" href="https://github.com/Arize-ai/phoenix/pull/9936" icon="github" horizontal>
GitHub
</Card>
