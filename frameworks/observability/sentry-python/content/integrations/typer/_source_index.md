---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/typer/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.055446Z"
---
# Index

---
title: Typer
description: Learn how to use Sentry to capture Typer exceptions.
---

The `TyperIntegration` captures exceptions raised when using [Typer CLI](https://typer.tiangolo.com/) applications.

## Install

Install Typer and the Sentry Python SDK.

```bash {tabTitle:pip}
pip install "sentry-sdk" "typer"
```
```bash {tabTitle:uv}
uv add "sentry-sdk" "typer"
```

## Configure

To enable the `TyperIntegration`, add it to the `integrations` list of your `sentry_sdk.init`. 

```python
import sentry_sdk
from sentry_sdk.integrations.typer import TyperIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[TyperIntegration()],
)
```

## Verify

Create a small CLI application:

```python
import typer
import sentry_sdk
from sentry_sdk.integrations.typer import TyperIntegration

sentry_sdk.init(...)  # see above

def main():
    1 / 0

if __name__ == "__main__":
    typer.run(main)
```

When you run this, Sentry will capture the `ZeroDivisionError` from the `main()`
function and you'll be able to see it on [sentry.io](https://sentry.io).
