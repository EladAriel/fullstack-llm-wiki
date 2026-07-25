---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2025/04-16-2025-api-key-generation-via-api.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.899128Z"
---
# 04 16 2025 Api Key Generation Via Api

---
title: "04.16.2025: API key generation via API"
description: Available in Phoenix 8.26+
---

<Update label="04.16.2025">

## API Key Generation Via API

Phoenix now supports programmatic API key creation through a new endpoint, making it easier to automate project setup and trace logging. To enable this, set the `PHOENIX_ADMIN_SECRET` environment variable in your deployment.

<Card title="Release arize-phoenix: v8.26.0 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/releases/tag/arize-phoenix-v8.26.0" horizontal>
  GitHub
</Card>

### Improvements and Bug Fixes 🐛

* [**Tracing**](https://github.com/Arize-ai/phoenix/pull/7132): Add load more and loading state to the infinite scroll
* [**UI**](https://github.com/Arize-ai/phoenix/pull/7167): Hide menu for changing role for self in UsersTable
* [**Security**](https://github.com/Arize-ai/phoenix/pull/7165): Prevent admins from changing their own roles
* [**Infrastructure**](https://github.com/Arize-ai/phoenix/pull/7172): Remove WebSocket dependency and migrate to Multipart Subscriptions
</Update>
