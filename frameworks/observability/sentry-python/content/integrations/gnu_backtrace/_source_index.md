---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/gnu_backtrace/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.061515Z"
---
# Index

---
title: GNU Backtrace
description: "Learn about the GNU backtrace integration and how to add it to your integrations list."
---

The GNU backtrace integration parses native stack trace produced by [`backtrace_symbols`](https://linux.die.net/man/3/backtrace_symbols) from error messages and concatenates them with the Python traceback.

It is currently tested to work with server exceptions raised by [`clickhouse-driver`](https://github.com/mymarilyn/clickhouse-driver).

## Install

Install `sentry-sdk` from PyPI.

```bash {tabTitle:pip}
pip install "sentry-sdk"
```
```bash {tabTitle:uv}
uv add "sentry-sdk"
```

## Configure

Add `GnuBacktraceIntegration()` to your `integrations` list:


```python
import sentry_sdk
from sentry_sdk.integrations.gnu_backtrace import GnuBacktraceIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[
        GnuBacktraceIntegration(),
    ],
)
```

## Verify

The GNU backtrace integration is tested with server exceptions raised by [`clickhouse-driver`](https://github.com/mymarilyn/clickhouse-driver).

Other libraries must emit exceptions that have backtrace-compatible values for the GNU backtrace integration to parse the exceptions.
