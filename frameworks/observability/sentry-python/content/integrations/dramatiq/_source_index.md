---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/dramatiq/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.052596Z"
---
# Index

---
title: Dramatiq
description: "Learn how to import and use the Dramatiq integration."
---

The Dramatiq integration adds support for the [Dramatiq](https://dramatiq.io/) background tasks library.

The Dramatiq integration only reports errors. Tracing is not yet supported. If you want to have more instrumentation, you need to do [custom instrumentation](/platforms/python/tracing/instrumentation/custom-instrumentation/).

<Alert>
  This is the successor of the original `DramatiqIntegration` that can be found here: https://github.com/jacobsvante/sentry-dramatiq

  The original maintainer has [donated the integration to Sentry](https://github.com/getsentry/sentry-python/issues/3387), so we can take over maintenance.
</Alert>

## Install

To get started, install `sentry-sdk` from PyPI.

```bash {tabTitle:pip}
pip install "sentry-sdk"
```
```bash {tabTitle:uv}
uv add "sentry-sdk"
```

## Configure

Add `DramatiqIntegration()` to your `integrations` list:


```python
import sentry_sdk
from sentry_sdk.integrations.dramatiq import DramatiqIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[
        DramatiqIntegration(),
    ],
)
```

## Verify

Trigger an error in your code to verify that the integration is sending events to Sentry.

```python
import dramatiq

import sentry_sdk
sentry_sdk.init(...)  # same as above

@dramatiq.actor(max_retries=0)
def dummy_actor(x, y):
    return x / y

dummy_actor.send(5, 0)
```

Running this will create an error event (`ZeroDivisionError`) that you should be able to see in [sentry.io](https://sentry.io).

## Supported Versions

- Dramatiq: 1.13+
- Python: 3.6+

<Include name="python-use-older-sdk-for-legacy-support.mdx" />
