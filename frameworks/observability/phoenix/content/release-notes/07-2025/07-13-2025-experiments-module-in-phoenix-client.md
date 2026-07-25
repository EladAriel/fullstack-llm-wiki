---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/07-2025/07-13-2025-experiments-module-in-phoenix-client.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.901984Z"
---
# 07 13 2025 Experiments Module In Phoenix Client

---
title: "07.13.2025: Experiments module in phoenix-client"
description: Available in Phoenix 11.7+
---

<Update label="07.13.2025">

## Experiments Module in phoenix-client

<Card title="arize-phoenix-client" href="https://pypi.org/project/arize-phoenix-client/" icon="cube" horizontal>
  PyPI
</Card>

**New Features in Phoenix 11.7+:**

* Added a new `experiments` property to both `Client` and `AsyncClient` for invoking experiment workflows.

* Introduced `Experiments` and `AsyncExperiments` classes with `run_experiment` methods supporting **tasks**, **evaluators**, **dry-run mode**, and **metadata**.

* Implemented `SyncExecutor` and `AsyncExecutor` classes for **concurrent execution** with built-in **progress bars**.

* Added `RateLimiter` and `AdaptiveTokenBucket` for intelligent handling and throttling of **rate-limit errors**.

**Bug Fixes:**

* Fixed a typo in the `datasets.get_dataset_versions` docstring.

**Enhancements:**

* Introduced a `PhoenixException` base class and **refactored exception imports** for consistency.

* Simplified rate limiter output by replacing `printif` with direct print statements.


<Card title="feat: Add experiments module to phoenix-client by anticorrelator · Pull Request #8375 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/8375" horizontal>
  GitHub
</Card>
</Update>