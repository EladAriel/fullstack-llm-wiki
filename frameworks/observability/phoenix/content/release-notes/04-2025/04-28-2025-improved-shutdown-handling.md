---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2025/04-28-2025-improved-shutdown-handling.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.842169Z"
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

