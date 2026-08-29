---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/sqlalchemy/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.058246Z"
---
# Index

---
title: SQLAlchemy
description: "Learn about importing the SQLAlchemy integration and how it captures queries from SQLAlchemy as breadcrumbs."
---

The SQLAlchemy integration captures queries from [SQLAlchemy](https://www.sqlalchemy.org/) as breadcrumbs and spans.

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

The SQLAlchemy integration is enabled automatically if you have the `sqlalchemy` package installed.

<PlatformContent includePath="getting-started-config" />

## Verify

```python
from sqlalchemy import create_engine
from sqlalchemy.sql import text

def main():
    sentry_sdk.init(...)  # same as above

    engine = create_engine(DATABASE_URL, echo=True)
    statement = text("SELECT 'Hello World'")

    with engine.connect() as conn:
        # or sentry_sdk.traces.start_span(name="testing_sentry", parent_span=None) in stream mode
        with sentry_sdk.start_transaction(name="testing_sentry"):
            result = conn.execute(statement)

main()
```

This will create a transaction called `testing_sentry` in the Performance section of [sentry.io](https://sentry.io) and will create a span for the `SELECT` statement.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Supported Versions

- SQLAlchemy: 1.2+
- Python: 3.6+

<Include name="python-use-older-sdk-for-legacy-support.mdx" />
