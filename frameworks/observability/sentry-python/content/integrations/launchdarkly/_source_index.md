---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/launchdarkly/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.061875Z"
---
# Index

---
title: LaunchDarkly
description: "Learn how to use Sentry with LaunchDarkly."
---

The [LaunchDarkly](https://launchdarkly.com/) integration tracks feature flag evaluations produced by the LaunchDarkly SDK. These evaluations are held in memory and are sent to Sentry on error and transaction events. **At the moment, we only support boolean flag evaluations.**

## Install

Install `sentry-sdk` from PyPI:

```bash {tabTitle:pip}
pip install sentry-sdk
```
```bash {tabTitle:uv}
uv add sentry-sdk
```

## Configure

Add `LaunchDarklyIntegration()` to your `integrations` list:

```python
import sentry_sdk
from sentry_sdk.integrations.launchdarkly import LaunchDarklyIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[
        LaunchDarklyIntegration(),
    ],
)
```

## Verify

The integration is tested by evaluating a feature flag using your LaunchDarkly SDK before capturing an exception.

```python
import ldclient
import sentry_sdk

client = ldclient.get()
client.variation("hello", Context.create("test-context"), False)

sentry_sdk.capture_exception(Exception("Something went wrong!"))
```

Visit the Sentry website and confirm that your error event has recorded the feature flag "hello" and its value "false".

## Supported Versions

- launchdarkly-server-sdk >= 9.8.0
- sentry-sdk >= 2.19.2
- python >= 3.8

<PlatformContent includePath="feature-flags/next-steps" />
