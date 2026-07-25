---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/tracing/instrumentation/custom-instrumentation/requests-module.mdx"
source_commit: "8557ccbd46b02c43301ef74ff54516736ecf9d69"
source_commit_short: "8557ccb"
source_commit_date: "2026-07-24T13:12:02-04:00"
generated_at: "2026-07-25T19:08:13.535970Z"
---
# Requests Module

---
title: Instrument HTTP Requests
sidebar_order: 2000
description: "Learn how to manually instrument your code to use Sentry's Requests module."
---
As a prerequisite to setting up [Requests](/product/dashboards/sentry-dashboards/outbound-api-requests/), you’ll need to first <PlatformLink to="/tracing/">set up tracing</PlatformLink>. Once this is done, the Python SDK will automatically instrument outgoing HTTP requests made via `HTTPConnection` and show the data in the [requests-monitoring dashboard](https://sentry.io/orgredirect/organizations/:orgslug/dashboards/). If that doesn't fit your use case, you can set up using custom instrumentation described below.

## Custom Instrumentation

For detailed information about which data can be set, see the [Requests Module developer specifications](https://develop.sentry.dev/sdk/performance/modules/requests/).

### Wrap HTTP Requests in a Span

NOTE: Refer to [HTTP Span Data Conventions](https://develop.sentry.dev/sdk/performance/span-data-conventions/#http) for a full list of the span data attributes.

Here is an example of an instrumented function that makes HTTP requests:

```python
from urllib.parse import urlparse
import requests

def make_request(method, url):
    span = sentry_sdk.start_span(
        op="http.client",
        name="%s %s" % (method, url),
    )

    span.set_data("http.request.method", method)

    parsed_url = urlparse(url)
    span.set_data("url", url)
    span.set_data("server.address", parsed_url.hostname)
    span.set_data("server.port", parsed_url.port)

    response = requests.request(method=method, url=url)

    span.set_data("http.response.status_code", response.status_code)
    span.set_data("http.response_content_length", response.headers["content-length"])

    span.finish()

    return response

```
