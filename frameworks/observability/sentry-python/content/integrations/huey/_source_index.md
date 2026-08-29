---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/huey/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.056191Z"
---
---
title: huey
description: "Learn how to import and use the huey integration."
---

The huey integration adds support for the
[huey task queue library](https://huey.readthedocs.io/en/latest/).

<Include name="python-stream-mode-general-callout.mdx" />

## Install

To get started, install `sentry-sdk` from PyPI.

```bash {tabTitle:pip}
pip install "sentry-sdk"
```

```bash {tabTitle:uv}
uv add "sentry-sdk"
```

## Configure

The huey integration is enabled automatically if you have the `huey` package installed.

<PlatformContent includePath="getting-started-config" />

## Verify

```python
from huey import SqliteHuey

sentry_sdk.init(...)  # same as above

huey = SqliteHuey(filename='demo.db')

@huey.task()
def add(a, b):
    return a + b

# or sentry_sdk.traces.start_span(name="your_span_name", parent_span=None) in stream mode
with sentry_sdk.start_transaction(name="testing_huey"):
    result = add(1, 2)
```

Running this will create a new transaction called `testing_huey` in the
Performance section of [sentry.io](https://sentry.io). It may
take a couple of moments for the transaction to show up.

## Supported Versions

- huey: 2.0+
- Python: 3.6+

<Include name="python-use-older-sdk-for-legacy-support.mdx" />
