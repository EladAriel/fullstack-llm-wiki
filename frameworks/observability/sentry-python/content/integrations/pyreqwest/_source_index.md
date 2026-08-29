---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/pyreqwest/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.061695Z"
---
---
title: pyreqwest
description: "Learn about the pyreqwest integration and how it adds support for the pyreqwest HTTP client."
---

The [pyreqwest](https://markussintonen.github.io/pyreqwest/pyreqwest.html) integration instruments outgoing HTTP requests using either the sync or the async pyreqwest client.

Use this integration to create spans for outgoing requests and ensure traces are properly propagated to downstream services.

<Include name="python-stream-mode-general-callout.mdx" />

## Install

Install `sentry-sdk` from PyPI:

```bash {tabTitle:pip}
pip install sentry-sdk
```

```bash {tabTitle:uv}
uv add sentry-sdk
```

## Configure

To enable the pyreqwest integration, add `PyreqwestIntegration` to your `integrations`:

```python
import sentry_sdk
from sentry_sdk.integrations.pyreqwest import PyreqwestIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[
        PyreqwestIntegration(),
    ],
)
```

## Verify

```python
import asyncio

from pyreqwest.client import ClientBuilder, SyncClientBuilder

sentry_sdk.init(...)  # same as above

async def example_async():
    async with ClientBuilder().error_for_status(True).build() as client:
        response = await client.get("http://example.com").build().send()

def example_sync():
    with SyncClientBuilder().error_for_status(True).build() as client:
        response = client.get("http://example.com").build().send()

# or sentry_sdk.traces.start_span(name="your_span_name", parent_span=None) in stream mode
with sentry_sdk.start_transaction(name="pyreqwest async"):
    asyncio.run(example_async())

# or sentry_sdk.traces.start_span(name="your_span_name", parent_span=None) in stream mode
with sentry_sdk.start_transaction(name="pyreqwest sync"):
    example_sync()

```

This will create two transactions, `pyreqwest async` and `pyreqwest sync`, in the Traces section of [sentry.io](https://sentry.io), and create spans for the outgoing HTTP requests.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Supported Versions

- pyreqwest: 0.11.6+
- Python: 3.11+
