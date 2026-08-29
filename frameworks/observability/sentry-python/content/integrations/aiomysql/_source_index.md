---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/aiomysql/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.061328Z"
---
# Index

---
title: aiomysql
description: "Learn about importing the aiomysql integration and how it captures queries from aiomysql as spans."
---

The aiomysql integration captures queries from [aiomysql](https://github.com/aio-libs/aiomysql/) as spans.

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

Add `AioMySQLIntegration()` to your `integrations` list:

```python
import sentry_sdk
from sentry_sdk.integrations.aiomysql import AioMySQLIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Add data like inputs and responses;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[
        AioMySQLIntegration(),
    ],
)
```

## Verify

```python
import sentry_sdk
from sentry_sdk.integrations.aiomysql import AioMySQLIntegration
import aiomysql
import asyncio

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    traces_sample_rate=1.0,
    send_default_pii=True,
    integrations=[
        AioMySQLIntegration(),
    ],
)

async def main():
    conn = await aiomysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        db="test",
    )
    try:
        # or sentry_sdk.traces.start_span(name="testing_sentry", parent_span=None) in stream mode
        with sentry_sdk.start_transaction(name="testing_sentry"):
            async with conn.cursor() as cur:
                await cur.execute("SELECT 'Hello World'")
                result = await cur.fetchone()
    finally:
        conn.close()

asyncio.run(main())
```

This will create a transaction called `testing_sentry` in the Performance section of [sentry.io](https://sentry.io) and will create a span for the `SELECT` statement.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Supported Versions

- aiomysql: 0.3+

<Include name="python-use-older-sdk-for-legacy-support.mdx" />
