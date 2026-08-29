---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/asyncpg/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.060261Z"
---
# Index

---
title: asyncpg
description: "Learn about importing the asyncpg integration and how it captures queries from asyncpg."
---

The `AsyncPGIntegration` captures queries from
[asyncpg](https://github.com/MagicStack/asyncpg), which can be viewed in Sentry's **Performance** page.

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

If you have the `asyncpg` package in your dependencies, the asyncpg integration will be enabled automatically when you initialize the Sentry SDK.

<PlatformContent includePath="getting-started-config" />

## Verify

```python
import asyncpg

async def main():
    sentry_sdk.init(...)  # same as above

    # or sentry_sdk.traces.start_span(name="testing_sentry", parent_span=None) in stream mode
    with sentry_sdk.start_transaction(name="testing_sentry"):
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.fetch("SELECT * FROM pg_catalog.pg_tables;")
        await conn.close()

asyncio.run(main())
```

This will create a transaction called `testing_sentry` in the Performance section of [sentry.io](https://sentry.io), and create spans for the `connect` and the `SELECT` operations.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Supported Versions

- asyncpg: 0.23+
- Python: 3.7+
