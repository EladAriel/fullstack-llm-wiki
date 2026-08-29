---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/aiohttp/aiohttp-client.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.063603Z"
---
# Aiohttp Client

---
title: AIOHTTP Client
description: "Learn about the AIOHTTP integration and how it adds support for the AIOHTTP HTTP client."
---

The [AIOHTTP](https://docs.aiohttp.org/en/stable/) integration instruments outgoing HTTP requests using the AIOHTTP client.

Use this integration to create spans for outgoing requests and ensure traces are properly propagated to downstream services.

This integration also supports AIOHTTP servers. See <PlatformLink to="/integrations/aiohttp/">AIOHTTP server documentation</PlatformLink> for details.

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

If you have the `aiohttp` package in your dependencies, the AIOHTTP integration will be enabled automatically when you initialize the Sentry SDK.

<PlatformContent includePath="getting-started-config" />

## Verify

```python
import asyncio
import aiohttp

async def main():
    sentry_sdk.init(...)  # same as above

    # or sentry_sdk.traces.start_span(name="your_span_name", parent_span=None) in stream mode
    with sentry_sdk.start_transaction(name="testing_sentry"):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://sentry.io/") as response:
                print("Status:", response.status)
            async with session.post("http://httpbin.org/post") as response:
                print("Status:", response.status)

asyncio.run(main())
```

This will create a transaction called `testing_sentry` in the Performance section of [sentry.io](https://sentry.io) and will create spans for the outgoing HTTP requests.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Supported Versions

- AIOHTTP: 3.5+
- Python: 3.7+
