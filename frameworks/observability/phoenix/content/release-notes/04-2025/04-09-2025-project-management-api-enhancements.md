---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2025/04-09-2025-project-management-api-enhancements.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.898754Z"
---
# 04 09 2025 Project Management Api Enhancements

---
title: "04.09.2025: Project management API enhancements"
description: Available in Phoenix 8.24+
---

<Update label="04.09.2025">

## Project Management API Enhancements

This update enhances the Project Management API with more flexible project identification:

* **Enhanced project identification**: Added support for identifying projects by both ID and hex-encoded name and introduced a new `get_project_by_identifier` helper function

Also includes streamlined operations, better validation & error handling, and expanded test coverage.

<Card title="feat: allow project name as identifier in REST path by RogerHYang · Pull Request #7064 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/7064" horizontal>
  GitHub
</Card>

### Improvements and Bug Fixes 🐛

* [**Performance**](https://github.com/Arize-ai/phoenix/pull/7107): Restore streaming
* [**Playground**](https://github.com/Arize-ai/phoenix/pull/7102): update Gemini models
* [**Enhancement**](https://github.com/Arize-ai/phoenix/pull/7089): Route user to forgot-password page in welcome email url
</Update>


