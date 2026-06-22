---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/advanced/testing-events.md"
source_commit: "0cb4a8e284b450abbccb71c543ad7757de46c0b2"
source_commit_short: "0cb4a8e2"
source_commit_date: "2026-06-20T16:31:34Z"
generated_at: "2026-06-21T07:06:10Z"
---

# Testing Events: lifespan and startup - shutdown { #testing-events-lifespan-and-startup-shutdown }

When you need `lifespan` to run in your tests, you can use the `TestClient` with a `with` statement:

{* ../../docs_src/app_testing/tutorial004_py310.py hl[9:15,18,27:28,30:32,41:43] *}


You can read more details about the ["Running lifespan in tests in the official Starlette documentation site."](https://www.starlette.dev/lifespan/#running-lifespan-in-tests)

For the deprecated `startup` and `shutdown` events, you can use the `TestClient` as follows:

{* ../../docs_src/app_testing/tutorial003_py310.py hl[9:12,20:24] *}
