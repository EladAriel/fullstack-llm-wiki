---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/unleash/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.056751Z"
---
# Index

---
title: Unleash
description: "Learn how to use Sentry with Unleash."
---

The [Unleash](https://www.getunleash.io/) integration tracks feature flag evaluations produced by the Unleash SDK. These evaluations are held in memory and are sent to Sentry on error and transaction events. **At the moment, we only support boolean flag evaluations from Unleash's is_enabled method.**

## Install

Install `sentry-sdk` from PyPI:

```bash {tabTitle:pip}
pip install sentry-sdk
```
```bash {tabTitle:uv}
uv add sentry-sdk
```

## Configure

Add `UnleashIntegration` to your `integrations` list:

```python
import sentry_sdk
from sentry_sdk.integrations.unleash import UnleashIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[UnleashIntegration()],
)
```

For more information on how to use Unleash, read Unleash's [Python reference](https://docs.getunleash.io/reference/sdks/python) and [quickstart guide](https://docs.getunleash.io/quickstart).

## Verify

Test the integration by evaluating a feature flag using your Unleash SDK before capturing an exception.

```python
import sentry_sdk
from UnleashClient import UnleashClient

unleash = UnleashClient(...)  # See Unleash quickstart.
unleash.initialize_client()

test_flag_enabled = unleash.is_enabled("test-flag")
sentry_sdk.capture_exception(Exception("Something went wrong!"))
```

Visit the [Sentry website](https://sentry.io/issues/) and confirm that your error
event has recorded the feature flag "test-flag", and its value is equal to `test_flag_enabled`.

## Supported Versions

- UnleashClient >= 6.0.1
- sentry-sdk >= 2.20.0
- python >= 3.8

<PlatformContent includePath="feature-flags/next-steps" />
