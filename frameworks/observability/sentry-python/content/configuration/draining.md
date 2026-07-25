---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/configuration/draining.mdx"
source_commit: "8557ccbd46b02c43301ef74ff54516736ecf9d69"
source_commit_short: "8557ccb"
source_commit_date: "2026-07-24T13:12:02-04:00"
generated_at: "2026-07-25T19:08:13.514547Z"
---
# Draining

---
title: Shutdown and Draining
sidebar_order: 80
description: "Learn more about the default behavior of our SDK if the application shuts down unexpectedly."
---

By default the SDK sends out events over the network on a background thread. This means that some events might be lost if the application shuts down unexpectedly. The SDK provides mechanisms to cope with this.

The Python SDK automatically drains on shutdown unless the `AtexitIntegration` is removed or the `shutdown_timeout`
config key is set to 0. If you need to manually drain, the client provides a `close` method:

```python
import sentry_sdk

client = sentry_sdk.get_client()
client.close(timeout=2.0)
```

After a call to `close`, the client  is disabled. It's important to
only call `close` immediately before shutting down the application.

Alternatively, the `flush` method drains the event queue while keeping the
client enabled for continued use.
