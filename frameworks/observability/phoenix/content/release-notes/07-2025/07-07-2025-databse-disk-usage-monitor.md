---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/07-2025/07-07-2025-databse-disk-usage-monitor.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.902564Z"
---
# 07 07 2025 Databse Disk Usage Monitor

---
title: "07.07.2025: Database disk usage monitor"
description: Available in Phoenix 11.5+
---

<Update label="07.07.2025" description="">

## Database Disk Usage Monitor

**New Features:**

* Added a **disk usage monitor daemon** that periodically checks storage consumption.

* Sends **warning emails** to administrators when usage crosses a configured threshold.

* **Blocks insert/update operations** when usage exceeds a higher critical threshold.

* Introduced **configurable environment variables** for warning and blocking thresholds with validation.

* Integrated disk usage checks into both the **FastAPI app** and **gRPC serve** to enforce write blocked.

**Enhancements:**

* Extended the email sender with a method and HTML template specifically for **disk usage alert notifications**.

<Card title="feat: add database disk usage monitor by RogerHYang · Pull Request #8402 · Arize-ai/phoenix" href="https://github.com/Arize-ai/phoenix/pull/8402" icon="github" horizontal description="Database disk usage monitor"/>
</Update>