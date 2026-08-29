---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/clickhouse-driver/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.052413Z"
---
# Index

---
title: clickhouse-driver
description: "Learn about importing the clickhouse-driver integration and how it captures queries from clickhouse-driver as breadcrumbs."
---

The clickhouse-driver integration captures queries from
[clickhouse-driver](https://github.com/mymarilyn/clickhouse-driver) as breadcrumbs and spans.
The integration is available for clickhouse-driver 0.2.0 or later.

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

If you have the `clickhouse-driver` package in your dependencies, the clickhouse-driver integration will be enabled automatically when you initialize the Sentry SDK.

<PlatformContent includePath="getting-started-config" />

By default, the parameters of the query are not retrieved. To see the query parameters in Sentry, enable `send_default_pii`. See <PlatformLink to="/configuration/options/#send-default-pii">Basic Options</PlatformLink> for details.

## Verify

```python
from clickhouse_driver import Client

def main():
    sentry_init(...)  # same as above

    # or sentry_sdk.traces.start_span(name="your_span_name", parent_span=None) in stream mode
    with sentry_sdk.start_transaction(name="testing_sentry"):
        client = Client(host=DATABASE_HOST)
        client.execute("DROP TABLE IF EXISTS sentry_test")
        client.execute("CREATE TABLE sentry_test (x Int32) ENGINE = Memory")
        client.execute("INSERT INTO sentry_test (x) VALUES", [{"x": 100}])

main()
```

This will create a transaction called `testing_sentry` in the Performance section of [sentry.io](https://sentry.io), and create spans for the database operations.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Supported Versions

- clickhouse-driver >= 0.2.0
- python >= 3.8
