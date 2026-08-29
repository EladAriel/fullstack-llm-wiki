---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/starlite/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.063043Z"
---
# Index

---
title: Starlite
description: "Learn about using Sentry with Starlite."
---

The Starlite integration adds support for the [Starlite framework](https://docs.litestar.dev/1/).

<Include name="python-stream-mode-general-callout.mdx" />

## Install

Install `sentry-sdk` from PyPI:

```bash {tabTitle:pip}
pip install sentry-sdk uvicorn
```

```bash {tabTitle:uv}
uv add sentry-sdk uvicorn
```

## Configure

If you have the `starlite` package in your dependencies, the Starlite integration will be enabled automatically when you initialize the Sentry SDK.

<PlatformContent includePath="getting-started-config" />

## Verify

```python
from starlite import Starlite, get

sentry_sdk.init(...)  # same as above

@get("/hello")
async def hello_world() -> str:
    1 / 0
    return "Hello!"

app = Starlite(route_handlers=[hello_world])
```

Save the file above as `app.py` and start the development server with:

```bash
uvicorn app:app
```

When you point your browser to [http://localhost:8000/hello](http://localhost:8000/hello) a transaction will be created in the Performance section of [sentry.io](https://sentry.io). Additionally, the `ZeroDivisionError` we've snuck into our `hello_world` handler will be sent to [sentry.io](https://sentry.io) and will be connected to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Supported Versions

<Alert level="warning" title="Note">

Starlite was renamed to Litestar with the release of version 2.0.
We support different integrations for each one. This guide applies to Starlite.
See [Litestar integration](/platforms/python/integrations/litestar) for the guide that applies to Litestar.

</Alert>

- Starlite: 1.48.0 - 1.51.14
- Python: 3.8+
