---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/configuration/draining__v1.x.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.037880Z"
---
# Draining__V1.X

---
title: Shutdown and Draining
sidebar_order: 80
description: "Learn more about the default behavior of our SDK if the application shuts down unexpectedly."
---

By default the SDK sends out events over the network on a background thread. This means that some events might be lost if the application shuts down unexpectedly. The SDK provides mechanisms to cope with this.

The Python SDK automatically drains on shutdown unless the `AtexitIntegration` is removed or the `shutdown_timeout`
config key is set to 0. To manually drain the client provides a `close` method:

```python
from sentry_sdk import Hub

client = Hub.current.client
if client is not None:
    client.close(timeout=2.0)
```

After a call to `close`, the client cannot be used anymore. It's important to
only call `close` immediately before shutting down the application.

Alternatively, the `flush` method drains the event queue while keeping the
client enabled for continued use.
