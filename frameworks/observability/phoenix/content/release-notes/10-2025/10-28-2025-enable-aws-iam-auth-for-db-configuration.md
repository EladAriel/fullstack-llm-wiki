---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/10-2025/10-28-2025-enable-aws-iam-auth-for-db-configuration.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.897155Z"
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
