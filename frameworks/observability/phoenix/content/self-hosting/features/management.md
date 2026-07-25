---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/features/management.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.939153Z"
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


