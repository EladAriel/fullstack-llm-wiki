---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/configuration/using-amazon-aurora.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.913502Z"
---
---
title: "Using Amazon Aurora"
description: "Phoenix supports IAM database authentication for PostgreSQL connections to Amazon Aurora/RDS."
---

<Info>
IAM database authentication for PostgreSQL (Aurora/RDS) is available since Phoenix **12.9.0**. Use that version or newer before following this guide.
</Info>

First, ensure that Phoenix runs with valid AWS credentials, either by using an IAM role attached to the instance (EC2/ECS/EKS), or by configuring `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Configuring `AWS_DEFAULT_REGION` is required.

The IAM role will need a `rds-db:connect` policy associated with it.

```bash
# Standard AWS configuration
export AWS_DEFAULT_REGION=us-east-2  ## REQUIRED
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
# OR use ~/.aws/credentials and ~/.aws/config
# OR use IAM role (EC2/ECS/EKS)
```

Then, configure Phoenix to use the Amazon Aurora/RDS instance with IAM-based authentication. No token-lifetime tuning is required; Phoenix generates a fresh IAM token for each new database connection.

```bash
# Enable IAM authentication
export PHOENIX_POSTGRES_USE_AWS_IAM_AUTH=true

# Database connection
export PHOENIX_POSTGRES_HOST=mydb.us-east-2.rds.amazonaws.com
export PHOENIX_POSTGRES_USER=iam_db_user
export PHOENIX_POSTGRES_DB=phoenix
```

