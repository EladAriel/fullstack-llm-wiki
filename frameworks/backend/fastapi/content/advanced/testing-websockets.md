---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/advanced/testing-websockets.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.705812Z"
---
# Testing WebSockets { #testing-websockets }

You can use the same `TestClient` to test WebSockets.

For this, you use the `TestClient` in a `with` statement, connecting to the WebSocket:

{* ../../docs_src/app_testing/tutorial002_py310.py hl[27:31] *}

/// note

For more details, check Starlette's documentation for [testing WebSockets](https://starlette.dev/testclient/#testing-websocket-sessions).

///
