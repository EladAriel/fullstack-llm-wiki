---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/features/management.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.917072Z"
---
# Management

---
title: "Management"
description: How to manage your Phoenix instance
---

API allows administrators to programmatically manage their instance. The management APIs are accessible to both system API keys as well as the `PHOENIX_ADMIN_SECRET`

### Authentication

Authenticate your API calls with a system key or admin secret

```bash
Authorization: Bearer $PHOENIX_ADMIN_SECRET
```

### API Reference

The API provides endpoints for creating, updating, and deleting users, projects, and more.

See the [REST API](/docs/phoenix/sdk-api-reference/rest-api/overview) for details.


