---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/advanced/testing-websockets.md"
source_commit: "0cb4a8e284b450abbccb71c543ad7757de46c0b2"
source_commit_short: "0cb4a8e2"
source_commit_date: "2026-06-20T16:31:34Z"
generated_at: "2026-06-21T07:06:10Z"
---

# Testing WebSockets { #testing-websockets }

You can use the same `TestClient` to test WebSockets.

For this, you use the `TestClient` in a `with` statement, connecting to the WebSocket:

{* ../../docs_src/app_testing/tutorial002_py310.py hl[27:31] *}

/// note

For more details, check Starlette's documentation for [testing WebSockets](https://www.starlette.dev/testclient/#testing-websocket-sessions).

///
