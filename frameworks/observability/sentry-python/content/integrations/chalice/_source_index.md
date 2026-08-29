---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/chalice/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.056011Z"
---
# Index

---
title: Chalice
description: "Learn about using Sentry with Chalice."
---

## Install

Install `sentry-sdk` from PyPI:

```bash {tabTitle:pip}
pip install sentry-sdk
```
```bash {tabTitle:uv}
uv add sentry-sdk
```

## Configure

If you have the `chalice` package in your dependencies, the Chalice integration will be enabled automatically when you initialize the Sentry SDK.

<PlatformContent includePath="getting-started-config" />

## Verify

```python
from chalice import Chalice

sentry_sdk.init(...)  # as above

app = Chalice(app_name="helloworld")

@app.schedule(Rate(1, unit=Rate.MINUTES))
def every_minute(event):
    1 / 0  # raises an error

@app.route("/")
def index():
    1 / 0  # raises an error
    return {"hello": "world"}
```

When you enter the `"/"` route or the scheduled task is run, an error event will be sent to [sentry.io](https://sentry.io).

## Behavior

- Request data is attached to all events: HTTP method, URL, headers, form data, JSON payloads. Sentry excludes raw bodies and multipart file uploads. Sentry also excludes personally identifiable information (such as user ids, usernames, cookies, authorization headers, IP addresses) unless you set send_default_pii to True.

- Each request has a separate scope. Changes to the scope within a view, for example setting a tag, will only apply to events sent as part of the request being handled.

## Supported Versions

- Chalice: 1.16.0+
- Python: 3.6+
