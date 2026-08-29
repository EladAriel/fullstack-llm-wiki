---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/quart/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.058608Z"
---
---
title: Quart
description: "Learn about using Sentry with Quart."
---

The Quart integration adds support for the [Quart Web Framework](https://gitlab.com/pgjones/quart).

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

If you have the `quart` package in your dependencies, the Quart integration will be enabled automatically when you initialize the Sentry SDK.

<PlatformContent includePath="getting-started-config" />

# Verify

```python
from quart import Quart

sentry_sdk.init(...)  # same as above

app = Quart(__name__)

@app.route("/")
async def hello():
    1/0  # raises an error
    return {"hello": "world"}

app.run()
```

When you point your browser to [http://localhost:5000/](http://localhost:5000/) a transaction in the Performance section of [sentry.io](https://sentry.io) will be created. Additionally, an error event will be sent to [sentry.io](https://sentry.io) and will be connected to the transaction.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Behavior

- The Sentry Python SDK will install the Quart integration for all of your apps.

- All exceptions leading to an Internal Server Error, from before/after serving functions, and background tasks are reported.

- Request data is attached to all events: **HTTP method, URL, headers**. Sentry also excludes personally identifiable information (such as user IDs, usernames, cookies, authorization headers, IP addresses) unless you set `send_default_pii` to `True`.

- Each request has a separate scope. Changes to the scope within a view, for example setting a tag, will only apply to events sent as part of the request being handled.

- Logging with any logger will create breadcrumbs when the [Logging](/platforms/python/integrations/logging/) integration is enabled (done by default).

## Supported Versions

- Quart: 0.16.1+
- Python: 3.7+
