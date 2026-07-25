---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/advanced/testing-events.md"
source_commit: "255b912928904e3ba5980425a54d6837c8bd1a1c"
source_commit_short: "255b9129"
source_commit_date: "2026-07-24T21:15:37Z"
generated_at: "2026-07-25T11:50:10Z"
---

# Testing Events: lifespan and startup - shutdown { #testing-events-lifespan-and-startup-shutdown }

When you need `lifespan` to run in your tests, you can use the `TestClient` with a `with` statement:

{* ../../docs_src/app_testing/tutorial004_py310.py hl[9:15,18,27:28,30:32,41:43] *}


You can read more details about the ["Running lifespan in tests in the official Starlette documentation site."](https://starlette.dev/lifespan/#running-lifespan-in-tests)

For the deprecated `startup` and `shutdown` events, you can use the `TestClient` as follows:

{* ../../docs_src/app_testing/tutorial003_py310.py hl[9:12,20:24] *}
