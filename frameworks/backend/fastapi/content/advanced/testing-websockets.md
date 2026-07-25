---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/advanced/testing-websockets.md"
source_commit: "255b912928904e3ba5980425a54d6837c8bd1a1c"
source_commit_short: "255b9129"
source_commit_date: "2026-07-24T21:15:37Z"
generated_at: "2026-07-25T11:50:10Z"
---

# Testing WebSockets { #testing-websockets }

You can use the same `TestClient` to test WebSockets.

For this, you use the `TestClient` in a `with` statement, connecting to the WebSocket:

{* ../../docs_src/app_testing/tutorial002_py310.py hl[27:31] *}

/// note

For more details, check Starlette's documentation for [testing WebSockets](https://starlette.dev/testclient/#testing-websocket-sessions).

///
