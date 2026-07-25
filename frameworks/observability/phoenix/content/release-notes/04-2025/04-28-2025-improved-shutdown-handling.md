---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2025/04-28-2025-improved-shutdown-handling.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.899849Z"
---
# 04 28 2025 Improved Shutdown Handling

---
title: "04.28.2025: Improved shutdown handling"
description: Available in Phoenix 8.28+
---

<Update label="04.28.2025">

## Improved Shutdown Handling

When stopping the Phoenix server via `Ctrl+C`, the shutdown process now exits cleanly without displaying a traceback or returning a non-zero exit code. Previously, a `KeyboardInterrupt` and `CancelledError` traceback could appear, ending the process with status code 130. The server now swallows the interrupt for a smoother shutdown experience, exiting with code 0 by default to reflect intentional termination.

<Card title="feat: gracefully handle ctrl-c by codefromthecrypt · Pull Request #7305 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/7305" horizontal>
  GitHub
</Card>

### Improvements and Bug Fixes 🐛

* [**Fix**](https://github.com/Arize-ai/phoenix/pull/7319)**:** Use Float for token count summaries
* [**Enhancement**](https://github.com/Arize-ai/phoenix/pull/7321): Improve browser compatibility for table sizing
* [**UX**](https://github.com/Arize-ai/phoenix/pull/7336): Simplify `homeLoaderQuery` to prevent idle timeout errors
</Update>

