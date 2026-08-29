---
type: "Framework Learn Page"
framework: "FastAPI"
source_repo: "https://github.com/fastapi/fastapi.git"
source_branch: "master"
source_path: "docs/en/docs/editor-support.md"
source_commit: "49033471594ea5d99a80abdf1043231b7791ee49"
source_commit_short: "4903347"
source_commit_date: "2026-08-26T17:53:57+00:00"
generated_at: "2026-08-29T09:38:49.700760Z"
---
# Editor Support { #editor-support }

The official [FastAPI Extension](https://marketplace.visualstudio.com/items?itemName=FastAPILabs.fastapi-vscode) enhances your FastAPI development workflow with *path operation* discovery, navigation, as well as FastAPI Cloud deployment, and live log streaming.

For more details about the extension, refer to the README on the [GitHub repository](https://github.com/fastapi/fastapi-vscode).

## Setup and Installation { #setup-and-installation }

The **FastAPI Extension** is available for both [VS Code](https://code.visualstudio.com/) and [Cursor](https://www.cursor.com/). It can be installed directly from the Extensions panel in each editor by searching for "FastAPI" and selecting the extension published by **FastAPI Labs**. The extension also works in browser-based editors such as [vscode.dev](https://vscode.dev) and [github.dev](https://github.dev).

### Application Discovery { #application-discovery }

By default, the extension will automatically discover FastAPI applications in your workspace by scanning for files that instantiate `FastAPI()`. If auto-detection doesn't work for your project structure, you can specify an entrypoint via `[tool.fastapi]` in `pyproject.toml` or the `fastapi.entryPoint` VS Code setting using module notation (e.g. `myapp.main:app`).

## Features { #features }

- **Path Operation Explorer** - A sidebar tree view of all <dfn title="routes, endpoints">*path operations*</dfn> in your application. Click to jump to any route or router definition.
- **Route Search** - Search by path, method, or name with <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd> (on macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd>).
- **CodeLens Navigation** - Clickable links above test client calls (e.g. `client.get('/items')`) that jump to the matching *path operation* for quick navigation between tests and implementation.
- **Deploy to FastAPI Cloud** - One-click deployment of your app to [FastAPI Cloud](https://fastapicloud.com/).
- **Stream Application Logs** - Real-time log streaming from your FastAPI Cloud-deployed application with level filtering and text search.

If you'd like to familiarize yourself with the extension's features, you can check out the extension walkthrough by opening the Command Palette (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> or on macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>) and selecting "Welcome: Open walkthrough..." and then choosing the "Get started with FastAPI" walkthrough.
