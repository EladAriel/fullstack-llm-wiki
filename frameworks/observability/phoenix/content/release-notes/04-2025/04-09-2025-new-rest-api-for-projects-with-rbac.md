---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2025/04-09-2025-new-rest-api-for-projects-with-rbac.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.898542Z"
---
# 04 09 2025 New Rest Api For Projects With Rbac

---
title: "04.09.2025: New REST API for projects with RBAC"
description: Available in Phoenix 8.23+
---

<Update label="04.09.2025">

## New REST API For Projects With RBAC

<Frame>
  <iframe
    src="https://cdn.iframe.ly/a2mKu6h"
    width={1000}
    height={400}
    allowFullScreen
    allow="encrypted-media *;"
  />
</Frame>

This release introduces a REST API for managing projects, complete with full CRUD functionality and access control. Key features include:

* **CRUD Operations:** Create, read, update, and delete projects via the new API endpoints.
* **Role-Based Access Control:**
  * Admins can create, read, update, and delete projects
  * Members can create and read projects, but cannot modify or delete them.
* **Additional Safeguards:** Immutable Project Names, Default Project Protection, Comprehensive Integration Tests

Check out our [new documentation](/docs/phoenix/sdk-api-reference/rest-api/api-reference/projects) to test these features.

<Card title="feat: REST API for CRUD operations on projects by RogerHYang · Pull Request #7006 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/7006" horizontal>
  GitHub
</Card>

### Improvements and Bug Fixes 🐛

* [**Phoenix Server**](https://github.com/Arize-ai/phoenix/issues/7051): add PHOENIX\_ALLOWED\_ORIGINS env
* [**Tracing**](https://github.com/Arize-ai/phoenix/issues/7085): Delete annotations in the feedback table, Make feedback table scrollable
* [**Experiments**](https://github.com/Arize-ai/phoenix/issues/7069): Allow scrolling the entire experiment compare table
* [**Projects**](https://github.com/Arize-ai/phoenix/issues/7066): Make time range selector more accessible
* [**Playground**](https://github.com/Arize-ai/phoenix/issues/7067): Don't close model settings dialog when picking Azure version
* [**Session**](https://github.com/Arize-ai/phoenix/issues/7072)**:** improve PostgreSQL error message in launch\_app
</Update>


