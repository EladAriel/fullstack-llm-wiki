---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/tracing/instrumentation/custom-instrumentation/requests-module.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.048912Z"
---
# Requests Module

---
title: Instrument HTTP Requests
sidebar_order: 2000
description: "Learn how to manually instrument your code to use Sentry's Requests module."
---

As a prerequisite to setting up [Requests](/product/dashboards/sentry-dashboards/outbound-api-requests/), you’ll need to first <PlatformLink to="/tracing/">set up tracing</PlatformLink>. Once this is done, the Python SDK will automatically instrument outgoing HTTP requests made via `HTTPConnection` and show the data in the [requests-monitoring dashboard](https://sentry.io/orgredirect/organizations/:orgslug/dashboards/). If that doesn't fit your use case, you can set up using custom instrumentation described below.

<Alert>

This page covers both transaction mode (default) and stream mode. See <PlatformLink to="/tracing/streamed-spans/">Streamed Spans</PlatformLink> to learn more.

</Alert>

## Custom Instrumentation

For detailed information about which data can be set, see the [Requests Module developer specifications](https://develop.sentry.dev/sdk/performance/modules/requests/).

### Wrap HTTP Requests in a Span

NOTE: Refer to [HTTP Span Data Conventions](https://develop.sentry.dev/sdk/performance/span-data-conventions/#http) for a full list of the span data attributes.

Here is an example of an instrumented function that makes HTTP requests:

```python {tabTitle:Transaction Mode (Default)}
from urllib.parse import urlparse
import requests
import sentry_sdk

def make_request(method, url):
    span = sentry_sdk.start_span(
        op="http.client",
        name=f"{method} {url}",
    )

    span.set_data("http.request.method", method)

    parsed_url = urlparse(url)
    span.set_data("url", url)
    span.set_data("server.address", parsed_url.hostname)
    span.set_data("server.port", parsed_url.port)

    response = requests.request(method=method, url=url)

    span.set_data("http.response.status_code", response.status_code)
    span.set_data("http.response_content_length", response.headers.get("content-length"))

    span.finish()

    return response

```

```python {tabTitle:Stream Mode}
from urllib.parse import urlparse
import requests
import sentry_sdk

def make_request(method, url):
    span = sentry_sdk.traces.start_span(
        name=f"{method} {url}",
        attributes={"sentry.op": "http.client"},
    )
    parsed_url = urlparse(url)
    span.set_attributes({
        "http.request.method": method,
        "url": url,
        "server.address": parsed_url.hostname,
        "server.port": parsed_url.port,
    })
    response = requests.request(method=method, url=url)

    span.set_attribute("http.response.status_code", response.status_code)

    content_length = response.headers.get("content-length")
    if content_length is not None:
        span.set_attribute("http.response.header.content-length", content_length)

    span.finish()
    return response
```
