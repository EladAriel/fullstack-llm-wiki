---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/arq/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.052972Z"
---
# Index

---
title: arq
description: "Learn about using Sentry with arq."
---

The arq integration adds support for the [arq job queue system](https://arq-docs.helpmanual.io/).

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

If you have the `arq` package in your dependencies, the arq integration will be enabled automatically when you initialize the Sentry SDK.

<PlatformContent includePath="getting-started-config" />

## Verify

### Enqueuing the jobs in `run.py`:

```python
import asyncio

from arq import create_pool
from arq.connections import RedisSettings

async def main():
    sentry_sdk.init(...)  # same as above
    redis = await create_pool(RedisSettings())

    # or sentry_sdk.traces.start_span(name="testing_sentry", parent_span=None) in stream mode
    with sentry_sdk.start_transaction(name="testing_sentry"):
        r = await redis.enqueue_job("add_numbers", 1, 2)

asyncio.run(main())
```

When you run `run.py` it will create a transaction called `testing_sentry` in the Performance section of [sentry.io](https://sentry.io), and create a span for enqueuing the job.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

### Job definition in `demo.py`:

```python
import sentry_sdk
from sentry_sdk.integrations.arq import ArqIntegration

sentry_sdk.init(...)  # same as above

async def add_numbers(ctx, a, b):
    1/0 # raises an error!
    return a + b

class WorkerSettings:
    functions = [add_numbers]
```

When you run a worker with `arq demo.WorkerSettings` it will create a transaction called `add_numbers` in the Performance section of [sentry.io](https://sentry.io), and will also create and issue in Sentry and connect it to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Supported Versions

- ARQ: 0.23+
- Python: 3.7+
