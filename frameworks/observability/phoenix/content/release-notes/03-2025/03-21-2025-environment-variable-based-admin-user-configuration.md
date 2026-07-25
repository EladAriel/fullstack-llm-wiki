---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/03-2025/03-21-2025-environment-variable-based-admin-user-configuration.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.890857Z"
---
# 03 21 2025 Environment Variable Based Admin User Configuration

---
title: "03.21.2025: Environment variable based admin user configuration"
description: Available in Phoenix 8.17+
---

<Update label="03.21.2025">

## Environment Variable Based Admin User Configuration

You can now specify one or more admin users at startup using an environment variable. This is especially useful for managed deployments, allowing you to define admin access in a manifest or configuration file. The specified users will be automatically seeded into the database, enabling immediate login without manual setup.

<Card title="Release arize-phoenix: v8.17.0 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/releases/tag/arize-phoenix-v8.17.0" horizontal>
  GitHub
</Card>

### Improvements and Bug Fixes 🐛

* [**Performance**](https://github.com/Arize-ai/phoenix/issues/6858)**:** Smaller page sizes
* [**Projects**](https://github.com/Arize-ai/phoenix/issues/6847): Improved performance on projects page
* [**Experiments**](https://github.com/Arize-ai/phoenix/issues/6865): Allow hover anywhere on experiment cell
* [**Annotations**](https://github.com/Arize-ai/phoenix/issues/6886)**:** Show metadata
* [**Feedback**](https://github.com/Arize-ai/phoenix/issues/6887)**:** Show full metadata
</Update>


