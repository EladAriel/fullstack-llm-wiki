---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/httpx2/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.057687Z"
---
# Index

---
title: HTTPX2
description: "Learn about the HTTPX2 integration and how it adds support for the HTTPX2 HTTP client."
---

The [HTTPX2](https://httpx2.pydantic.dev/) integration instruments outgoing HTTP requests using either the sync or the async HTTPX2 clients.

Use this integration to create spans for outgoing requests and ensure traces are properly propagated to downstream services.

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

The HTTPX2 integration is enabled automatically if you have the `httpx2` package installed.

<PlatformContent includePath="getting-started-config" />

## Verify

```python
import httpx2

def main():
    sentry_init(...)  # same as above
    # or sentry_sdk.traces.start_span(name="your_span_name", parent_span=None) in stream mode
    with sentry_sdk.start_transaction(name="testing_sentry"):
        r1 = httpx2.get("https://sentry.io/")
        r2 = httpx2.post("http://httpbin.org/post")

main()
```

This will create a transaction called `testing_sentry` in the Performance section of [sentry.io](https://sentry.io), and create spans for the outgoing HTTP requests.

It takes a couple of moments for the data to appear in [sentry.io](https://sentry.io).

## Supported Versions

- HTTPX2: 2.0+
- Python: 3.10+
